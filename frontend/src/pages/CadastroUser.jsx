import { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { makeApiCall } from "../services/api";
import { values } from "lodash";
import {
  Container,
  TextField,
  Button,
  Typography,
  Alert,
  Box,
  CircularProgress, // Importando o CircularProgress do MUI
} from "@mui/material";
import { useForm } from "react-hook-form";
import PropTypes from "prop-types";
import IMask from "imask"; // Importando o IMask

const CadastroUser = ({ tipo = "candidato" }) => {
  const [apiResponse, setApiResponse] = useState("");
  const [errorRequest, setErrorRequest] = useState(false);
  const [loading, setLoading] = useState(false); // Estado para controlar o loading
  const navigate = useNavigate();

  // Utilizando o react-hook-form para gerenciar os dados do formulário
  const {
    register,
    handleSubmit,
    formState: { errors },
    watch,
  } = useForm();

  // Referência para o campo CPF, utilizado para aplicar máscara
  const cpfRef = useRef(null);

  // Função para aplicar a máscara do CPF utilizando IMask
  useEffect(() => {
    if (cpfRef.current) {
      IMask(cpfRef.current, {
        mask: "000.000.000-00",
      });
    }
  }, []); // Executa apenas uma vez, quando o componente é montado

  // Função chamada ao enviar o formulário
  const onSubmit = async (data) => {
    data.tipo = tipo; // O tipo pode ser "candidato" ou "responsavel"

    // Define o loading como true para mostrar o indicador
    setLoading(true);

    // Chama o endpoint correto para cada tipo de usuário
    const endpoint = tipo === "candidato" ? "candidato/" : "responsavel/";

    // Chama a função que faz a requisição para o cadastro do usuário
    await makeApiCallCadastroUser(endpoint, data); // Passa os dados para a API
  };

  // Função para fazer a chamada à API para cadastrar o usuário
  const makeApiCallCadastroUser = async (endpoint, data) => {
    try {
      // Faz a chamada à API utilizando o método 'makeApiCall' da camada de serviço
      const response = await makeApiCall(endpoint, data, "POST");
      setApiResponse(JSON.stringify(response, null, 2)); // Exibe a resposta da API
      setErrorRequest(false); // Reseta o estado de erro

      // Verifica se o e-mail foi fornecido e, em caso positivo, chama a função de verificação de e-mail
      if (data.email) {
        // Usando diretamente o e-mail enviado pelo formulário
        await handleRequestVerification(data.email); // Envia o e-mail para verificação
      }

      // Mensagens de sucesso após o cadastro
      const successMessages = {
        cadastro: "Cadastro realizado com sucesso!",
        emailVerification: "Verificação de e-mail enviada com sucesso!",
      };

      // Redireciona para a página de login, passando as mensagens de sucesso
      navigate("/login", {
        state: { messages: successMessages },
      });
    } catch (error) {
      console.log("Error:", error);
      setApiResponse(error.response.data); // Exibe a mensagem de erro
      setErrorRequest(true); // Marca que ocorreu um erro
    } finally {
      setLoading(false); // Finaliza o loading após a requisição
    }
  };

  // Função para solicitar a verificação de email
  const handleRequestVerification = async (email) => {
    try {
      // Chama a API para enviar o token de verificação para o e-mail
      await makeApiCall(
        "verificar-email/enviar-token/",
        { email }, // Passa o e-mail para o payload da requisição
        "POST"
      );
      // Não há necessidade de exibir mensagem de sucesso, pois já é tratada na função de cadastro
    } catch (error) {
      console.error("Erro ao enviar o token de verificação:", error);
      alert("Erro ao solicitar verificação de e-mail.");
    }
  };

  // Função para exibir as mensagens de erro da API
  const errorMessages = values(apiResponse).map((message) => message[0]);

  // Monitorando o campo de senha para validar a confirmação
  const password = watch("password");

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" component="h1" gutterBottom>
        Cadastro de {tipo === "candidato" ? "Candidato" : "Responsável"}
      </Typography>

      {/* Exibe o alerta de erro caso ocorra alguma falha na requisição */}
      {errorRequest && (
        <Alert severity="error">
          {errorMessages.map((message, index) => (
            <Typography key={index}>{message}</Typography>
          ))}
        </Alert>
      )}

      {/* Verifica se está em processo de carregamento e exibe o indicador */}
      {loading ? (
        <Box display="flex" justifyContent="center" mt={2}>
          <CircularProgress />
        </Box>
      ) : (
        <form onSubmit={handleSubmit(onSubmit)}>
          <TextField
            label="Nome"
            variant="outlined"
            fullWidth
            margin="normal"
            {...register("first_name", { required: "O nome é obrigatório" })}
            error={!!errors.first_name}
            helperText={errors.first_name?.message}
          />
          <TextField
            label="Sobrenome"
            variant="outlined"
            fullWidth
            margin="normal"
            {...register("last_name", {
              required: "O sobrenome é obrigatório",
            })}
            error={!!errors.last_name}
            helperText={errors.last_name?.message}
          />
          <TextField
            label="E-mail"
            variant="outlined"
            fullWidth
            margin="normal"
            type="email"
            {...register("email", { required: "O e-mail é obrigatório" })}
            error={!!errors.email}
            helperText={errors.email?.message}
          />
          <TextField
            label="Senha"
            variant="outlined"
            fullWidth
            margin="normal"
            type="password"
            {...register("password", { required: "A senha é obrigatória" })}
            error={!!errors.password}
            helperText={errors.password?.message}
          />
          <TextField
            label="Confirmar Senha"
            variant="outlined"
            fullWidth
            margin="normal"
            type="password"
            {...register("confirm_password", {
              required: "A confirmação de senha é obrigatória",
              validate: (value) =>
                value === password || "As senhas não coincidem",
            })}
            error={!!errors.confirm_password}
            helperText={errors.confirm_password?.message}
          />

          <TextField
            label="CPF"
            variant="outlined"
            fullWidth
            margin="normal"
            inputRef={cpfRef} // Referência para o campo CPF
            {...register("cpf", {
              required: "O CPF é obrigatório",
              pattern: {
                value: /^\d{3}\.\d{3}\.\d{3}-\d{2}$/,
                message: "O CPF deve estar no formato 000.000.000-00",
              },
            })}
            error={!!errors.cpf}
            helperText={errors.cpf?.message}
          />
          <TextField
            label="Data de Nascimento"
            type="date"
            fullWidth
            margin="normal"
            {...register("data_nascimento", {
              required: "A data de nascimento é obrigatória",
            })}
            error={!!errors.data_nascimento}
            helperText={errors.data_nascimento?.message}
            InputLabelProps={{
              shrink: true,
            }}
          />

          <Box mt={2}>
            <Button variant="contained" color="primary" type="submit" fullWidth>
              Registrar
            </Button>
          </Box>
        </form>
      )}

      <Box mt={2}>
        <Button
          variant="outlined"
          color="primary"
          onClick={() => navigate("/")}
          fullWidth
        >
          Voltar
        </Button>
      </Box>
    </Container>
  );
};

// Validação da prop 'tipo' para garantir que seja uma string
CadastroUser.propTypes = {
  tipo: PropTypes.string,
};

export default CadastroUser;
