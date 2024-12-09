import axios from "axios";
import { getAccessToken } from "./utils";

const API_URL = "http://127.0.0.1:8000/api/v1/";

export const buscarEnderecoPorCep = async (cep) => {
  try {
    // Garante que o CEP seja tratado como uma string
    const cepString = String(cep.cep);
    // Remove qualquer caractere não numérico (mantém apenas os dígitos)
    const cepSemMascara = cepString.replace(/\D/g, ""); // Expressão regular para remover caracteres não numéricos

    if (cepSemMascara.length !== 8) {
      throw new Error("CEP inválido. Deve conter exatamente 8 dígitos.");
    }

    // Realiza a requisição para a API do VIACEP
    const response = await fetch(
      `https://viacep.com.br/ws/${cepSemMascara}/json/`
    );

    if (!response.ok) {
      throw new Error("Erro ao consultar a API do VIACEP");
    }

    const data = await response.json();

    if (data.erro) {
      throw new Error("CEP não encontrado");
    }

    return data; // Retorna o JSON com os dados do endereço
  } catch (error) {
    console.error("Erro na busca de endereço:", error.message);
    throw error;
  }
};

// Função genérica para chamadas à API
export const makeApiCall = async (endpoint, data = {}, method = "GET") => {
  const endpointCall = API_URL + endpoint;
  const accessToken = getAccessToken();
  const config = {
    method,
    url: `${endpointCall}`,
    headers: {
      Authorization: accessToken ? `Bearer ${accessToken}` : "", // Certificando que o token não é vazio
    },
  };

  if (method === "POST" || method === "PUT" || method === "PATCH") {
    config.data = data; // Adiciona os dados ao body para POST, PUT, PATCH
  }

  try {
    const response = await axios(config);
    return response.data;
  } catch (error) {
    console.error("Erro ao fazer a chamada à API:", error);
    if (error.response && error.response.status === 401) {
      throw new Error("Token de acesso inválido");
    }
    throw error;
  }
};

// Função específica para solicitação de redefinição de senha
export const requestPasswordReset = (email) => {
  return makeApiCall("resetar-senha/", { email }, "POST");
};

// Função específica para confirmação de redefinição de senha
export const confirmPasswordReset = (email, token, password) => {
  return makeApiCall(
    "resetar-senha/completo/",
    { email, token, password },
    "POST"
  );
};
