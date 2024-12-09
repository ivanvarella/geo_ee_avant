import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { Button, Typography, Alert, Box } from "@mui/material";
import { useForm } from "react-hook-form";
import { makeApiCall } from "../../services/api"; // Função genérica para chamadas à API
import { isLoggedIn } from "../../services/utils"; // Verifica se o usuário está logado (localStorage)

const VerifyEmail = () => {
  const location = useLocation(); // Captura informações da URL, como parâmetros
  const navigate = useNavigate(); // Permite redirecionar o usuário para outra página

  // Configuração do React Hook Form para gerenciar os dados do formulário
  const {
    register, // Registra campos do formulário
    handleSubmit, // Lida com a submissão do formulário
    // setError, // Configura mensagens de erro específicas para campos
    setValue, // Preenche os campos do formulário
    formState: { errors }, // Armazena os erros de validação do formulário
  } = useForm();

  // Estados para gerenciar o comportamento e a UI
  const [isLoading, setIsLoading] = useState(false); // Estado de carregamento durante a requisição
  const [apiError, setApiError] = useState([]); // Armazena mensagens de erro recebidas da API
  const [successMessage, setSuccessMessage] = useState(null); // Armazena a mensagem de sucesso

  // Função chamada ao submeter o formulário
  const onSubmit = async (data) => {
    const { token, email } = data; // Extrai o token e o email dos dados do formulário

    try {
      setIsLoading(true); // Ativa o estado de carregamento enquanto a requisição é processada

      // Faz a chamada à API para verificar o e-mail
      await makeApiCall(
        "verificar-email/validar-token/", // Endpoint da API
        { email, token }, // Dados enviados no corpo da requisição
        "POST" // Método HTTP
      );

      // Se a requisição for bem-sucedida, exibe a mensagem de sucesso
      setSuccessMessage("E-mail verificado com sucesso!");

      // Mensagens de sucesso após o cadastro -> próxima página
      const successMessages = {
        emailVerificationDone: "E-mail verificado com sucesso!",
      };

      // Redireciona o usuário baseado no estado de login
      if (isLoggedIn()) {
        navigate("/"); // Usuário logado -> Página principal
      } else {
        navigate("/login", {
          state: { messages: successMessages },
        }); // Usuário não logado -> Página de login
      }
    } catch (error) {
      // Trata erros recebidos da API
      const responseErrors = error.response?.data?.non_field_errors || []; // Erros genéricos
      const formattedErrors = Array.isArray(responseErrors)
        ? responseErrors
        : [responseErrors]; // Garante que os erros estejam em formato de array

      setApiError(formattedErrors); // Atualiza o estado com as mensagens de erro
    } finally {
      setIsLoading(false); // Desativa o estado de carregamento ao finalizar
    }
  };

  // useEffect para capturar os parâmetros da URL e determinar comportamentos iniciais
  useEffect(() => {
    const searchParams = new URLSearchParams(location.search); // Extrai os parâmetros da URL
    const token = searchParams.get("token"); // Captura o parâmetro 'token'
    const email = searchParams.get("email"); // Captura o parâmetro 'email'

    // Verifica se ambos os parâmetros existem
    if (!token || !email) {
      setApiError(["Token ou Email inválidos."]); // Define um erro genérico
    } else {
      // Preenche automaticamente os campos ocultos do formulário
      setValue("token", token);
      setValue("email", email);
    }
  }, [location.search, setValue]); // Reexecuta apenas se a URL mudar

  return (
    <Box>
      <Typography variant="h5" gutterBottom>
        Verificação de E-mail
      </Typography>

      <Typography variant="body1" gutterBottom>
        {/* Exibe o e-mail extraído da URL, para confirmação visual */}
        Email: {location.search.split("email=")[1]?.split("&")[0] || ""}
      </Typography>

      {/* Exibe mensagens de erro, se houver */}
      {apiError.length > 0 && (
        <Alert severity="error">
          {apiError.map((err, index) => (
            <div key={index}>{err}</div> // Renderiza cada erro em uma nova linha
          ))}
        </Alert>
      )}

      {/* Exibe mensagem de sucesso, se houver */}
      {successMessage && (
        <Alert severity="success">
          {successMessage} {/* Mostra a mensagem de sucesso */}
        </Alert>
      )}

      {/* Lógica condicional para exibir diferentes botões com base nos estados */}
      {apiError.length > 0 && !successMessage ? (
        <Box mt={2}>
          {apiError.includes("Token ou Email inválidos.") ? (
            <Button
              variant="contained"
              color="secondary"
              onClick={() => navigate("/perfil")}
              fullWidth
            >
              Solicitar verificação de Email
            </Button>
          ) : (
            <Button
              variant="contained"
              color="primary"
              onClick={() => navigate(isLoggedIn() ? "/" : "/login")}
              fullWidth
            >
              {isLoggedIn() ? "Ir para a Página Principal" : "Ir para Login"}
            </Button>
          )}
        </Box>
      ) : null}

      {/* Formulário para submissão dos dados */}
      {!successMessage && apiError.length === 0 && (
        <form onSubmit={handleSubmit(onSubmit)}>
          <Box>
            {/* Campos ocultos que armazenam o token e o e-mail extraídos da URL */}
            <input
              type="hidden"
              value={location.search.split("token=")[1]?.split("&")[0] || ""}
              {...register("token", { required: true })} // Registra o campo "token"
            />
            <input
              type="hidden"
              value={location.search.split("email=")[1]?.split("&")[0] || ""}
              {...register("email", { required: true })} // Registra o campo "email"
            />

            {/* Exibe erros relacionados ao token, se houver */}
            {errors.token && (
              <Alert severity="error">{errors.token.message}</Alert>
            )}

            {/* Botão para submeter o formulário */}
            <Button
              type="submit"
              variant="contained"
              color="primary"
              disabled={isLoading} // Desabilita enquanto a requisição está em andamento
              fullWidth
            >
              {isLoading ? "Verificando..." : "Verificar E-mail"}{" "}
              {/* Texto dinâmico */}
            </Button>
          </Box>
        </form>
      )}
    </Box>
  );
};

export default VerifyEmail;
