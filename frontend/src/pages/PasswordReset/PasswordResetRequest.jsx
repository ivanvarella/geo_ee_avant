import { useState } from "react";
import {
  TextField,
  Button,
  Typography,
  Alert,
  Box,
  CircularProgress,
} from "@mui/material";
import { requestPasswordReset } from "../../services/api"; // Importa a função para fazer a requisição à API
import { values } from "lodash"; // Importa lodash para manipular mensagens de erro
import { useNavigate } from "react-router-dom"; // Utilizado para redirecionar o usuário após a ação

const PasswordResetRequest = () => {
  // Estados para armazenar os dados do formulário, resposta da API e estado de erro
  const [email, setEmail] = useState("");
  const [apiResponse, setApiResponse] = useState(""); // Armazena a resposta da API (erro ou sucesso)
  const [errorRequest, setErrorRequest] = useState(false); // Indica se ocorreu um erro na requisição
  const [loading, setLoading] = useState(false); // Estado para controlar o loading
  const navigate = useNavigate(); // Hook do React Router para navegação

  // Atualiza o estado do e-mail sempre que o usuário digitar no campo
  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  // Função chamada ao enviar o formulário
  const handleSubmit = async (e) => {
    e.preventDefault(); // Previne o comportamento padrão do formulário (recarregar a página)
    setApiResponse(""); // Reseta a resposta da API
    setErrorRequest(false); // Reseta o estado de erro
    setLoading(true); // Inicia o loading

    try {
      // Faz a requisição para enviar o e-mail de redefinição de senha
      await requestPasswordReset(email);

      // Redireciona o usuário para uma página de confirmação com a mensagem e o e-mail
      navigate("/recuperar-senha-enviado", {
        state: { message: "Link para redefinição enviado com sucesso!", email },
      });
    } catch (error) {
      // Caso ocorra um erro, captura os detalhes da resposta da API
      if (error.response && error.response.data) {
        setApiResponse(error.response.data); // Armazena os dados do erro retornados pela API
      } else {
        // Caso o erro não tenha detalhes, exibe uma mensagem genérica
        setApiResponse({ general: ["Erro inesperado. Tente novamente."] });
      }
      setErrorRequest(true); // Define que houve um erro
    } finally {
      setLoading(false); // Finaliza o loading
    }
  };

  // Extrai mensagens de erro da resposta da API utilizando lodash
  const errorMessages = values(apiResponse).map((message) => message[0]);

  return (
    <Box>
      {/* Título da página */}
      <Typography variant="h5" gutterBottom>
        Redefinir Senha
      </Typography>

      {/* Exibe mensagens de erro se ocorrerem durante a requisição */}
      {errorRequest && (
        <Alert severity="error">
          {" "}
          {/* Componente de alerta para mensagens de erro */}
          {errorMessages.map((message, index) => (
            <Typography key={index}>{message}</Typography> // Renderiza cada mensagem de erro
          ))}
        </Alert>
      )}

      {/* Formulário para enviar o e-mail de redefinição */}
      <form onSubmit={handleSubmit}>
        <TextField
          label="Email" // Rótulo do campo
          type="email" // Tipo de entrada para validação automática de e-mail
          value={email} // O valor atual do campo é controlado pelo estado
          onChange={handleEmailChange} // Atualiza o estado quando o usuário digita
          required // Define o campo como obrigatório
          fullWidth // O campo ocupa a largura total disponível
          margin="normal" // Margem entre os elementos do formulário
        />

        <Box mt={2}>
          {/* Botão para enviar o formulário */}
          {loading ? (
            <Button variant="contained" fullWidth disabled>
              Enviando...
              <CircularProgress size={24} style={{ marginLeft: 16 }} />
            </Button>
          ) : (
            <Button type="submit" variant="contained" color="primary" fullWidth>
              Enviar código de redefinição
            </Button>
          )}
        </Box>
      </form>
    </Box>
  );
};

export default PasswordResetRequest;
