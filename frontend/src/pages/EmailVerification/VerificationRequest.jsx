import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { Button, Typography, Alert, Box } from "@mui/material";
import { makeApiCall } from "../../services/api"; // Função genérica para chamadas à API
import { isLoggedIn } from "../../services/utils"; // Funções utilitárias

const VerificationRequest = () => {
  const navigate = useNavigate(); // Permite redirecionar o usuário
  const [emailStatus, setEmailStatus] = useState(null); // Estado do status do email
  const [apiError, setApiError] = useState(null); // Estado para mensagens de erro
  const [isLoading, setIsLoading] = useState(false); // Estado para carregamento

  // Verifica se o usuário está autenticado
  useEffect(() => {
    if (!isLoggedIn()) {
      navigate("/login"); // Redireciona para login se não autenticado
    } else {
      fetchEmailStatus(); // Busca o status do email
    }
  }, [navigate]);

  // Função para buscar o status do email via API
  const fetchEmailStatus = async () => {
    try {
      setIsLoading(true);
      const data = await makeApiCall("candidato/"); // Requisição GET

      // Obtém o primeiro resultado da lista de candidatos
      const candidate = data?.results?.[0];

      // Verifica o campo correto do status do e-mail
      setEmailStatus(candidate?.is_email_verified ? "verified" : "unverified");
    } catch {
      setApiError("Erro ao buscar status do email. Tente novamente.");
    } finally {
      setIsLoading(false);
    }
  };

  // Função para solicitar a verificação de email
  const handleRequestVerification = async () => {
    try {
      setIsLoading(true);

      // Obtém o e-mail do usuário armazenado no localStorage
      const email = localStorage.getItem("user_email");
      if (!email) {
        throw new Error("Email do usuário não encontrado.");
      }

      // Faz a requisição POST com o payload correto
      await makeApiCall(
        "verificar-email/enviar-token/",
        { email }, // Payload enviado no corpo da requisição
        "POST"
      );

      setApiError(null);
      alert("Solicitação de verificação enviada com sucesso!");
    } catch {
      setApiError("Erro ao solicitar verificação. Tente novamente.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Box>
      <Typography variant="h5" gutterBottom>
        Solicitação de Verificação de Email
      </Typography>

      {/* Mensagens de erro */}
      {apiError && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {apiError}
        </Alert>
      )}

      {/* Exibe o status atual do email */}
      {emailStatus === "verified" ? (
        <Alert severity="success" sx={{ mb: 2 }}>
          O email {localStorage.getItem("user_email")} já foi verificado.
        </Alert>
      ) : emailStatus === "unverified" ? (
        <Alert severity="warning" sx={{ mb: 2 }}>
          O email {localStorage.getItem("user_email")} não foi verificado.
        </Alert>
      ) : null}

      {/* Botões para ações */}
      {emailStatus === "verified" ? (
        <Button
          variant="contained"
          color="primary"
          fullWidth
          onClick={() => navigate("/perfil")}
        >
          Ir para o Perfil
        </Button>
      ) : emailStatus === "unverified" ? (
        <Button
          variant="contained"
          color="secondary"
          fullWidth
          onClick={handleRequestVerification}
          disabled={isLoading}
        >
          {isLoading ? "Enviando..." : "Solicitar Verificação"}
        </Button>
      ) : null}
    </Box>
  );
};

export default VerificationRequest;
