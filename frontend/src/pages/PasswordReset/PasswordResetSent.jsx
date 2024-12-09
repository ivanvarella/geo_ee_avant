import { useState } from "react";
import { useForm } from "react-hook-form";
import { TextField, Button, Typography, Alert, Box } from "@mui/material";
import { useLocation, useNavigate } from "react-router-dom";
import { confirmPasswordReset } from "../../services/api";

const PasswordResetSent = () => {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();
  const [apiError, setApiError] = useState(""); // Para mensagens de erro da API
  const [isLoading, setIsLoading] = useState(false); // Para indicar se a requisição está em andamento

  const location = useLocation();
  const navigate = useNavigate();

  // Obtém o email do estado passado pela página anterior
  const email = location.state?.email || "";

  // Verifica se o campo de confirmação de senha corresponde à senha
  const password = watch("password");

  const onSubmit = async (data) => {
    const { token, password } = data;

    // Verificação de todos os campos necessários
    if (!email || !token || !password) {
      setApiError("Por favor, preencha todos os campos corretamente.");
      return;
    }

    setIsLoading(true);
    try {
      await confirmPasswordReset(email, token, password); // Chama a função da API
      navigate("/recuperar-senha-completo", {
        state: { message: "Senha redefinida com sucesso!" },
      });
    } catch (error) {
      // Captura mensagens de erro da API e exibe no frontend
      setApiError(error.response?.data || "Erro inesperado. Tente novamente.");
    } finally {
      setIsLoading(false);
    }
  };

  // Se o email não estiver presente, mostramos apenas o botão de voltar
  if (!email) {
    return (
      <Box>
        <Typography variant="h5" gutterBottom>
          Acesso inválido!
        </Typography>
        <Typography variant="body1" gutterBottom>
          Parece que você não iniciou o processo de recuperação de senha. Por
          favor, solicite um novo código de recuperação.
        </Typography>
        <Box mt={2}>
          <Button
            variant="outlined"
            color="secondary"
            onClick={() => navigate("/recuperar-senha")}
            fullWidth
          >
            Voltar para Reenviar Código
          </Button>
        </Box>
      </Box>
    );
  }

  return (
    <Box>
      <Typography variant="h5" gutterBottom>
        Inserir Código e Nova Senha
      </Typography>

      {apiError && (
        <Alert severity="error">
          {typeof apiError === "string"
            ? apiError
            : Object.values(apiError).map((msg, index) => (
                <Typography key={index}>{msg[0]}</Typography>
              ))}
        </Alert>
      )}

      <form onSubmit={handleSubmit(onSubmit)}>
        <TextField
          label="E-mail"
          value={email}
          InputProps={{ readOnly: true }} // Campo de email travado
          fullWidth
          margin="normal"
        />

        <TextField
          label="Código de Verificação"
          {...register("token", {
            required: "O código de verificação é obrigatório.",
          })}
          error={!!errors.token}
          helperText={errors.token?.message}
          fullWidth
          margin="normal"
        />

        <TextField
          label="Nova Senha"
          type="password"
          {...register("password", {
            required: "A senha é obrigatória.",
            minLength: {
              value: 6,
              message: "A senha deve ter pelo menos 6 caracteres.",
            },
          })}
          error={!!errors.password}
          helperText={errors.password?.message}
          fullWidth
          margin="normal"
        />

        <TextField
          label="Confirmar Nova Senha"
          type="password"
          {...register("confirmPassword", {
            required: "A confirmação de senha é obrigatória.",
            validate: (value) =>
              value === password || "As senhas digitadas não coincidem.",
          })}
          error={!!errors.confirmPassword}
          helperText={errors.confirmPassword?.message}
          fullWidth
          margin="normal"
        />

        <Box mt={2}>
          <Button
            type="submit"
            variant="contained"
            color="primary"
            fullWidth
            disabled={isLoading}
          >
            {isLoading ? "Redefinindo..." : "Redefinir Senha"}
          </Button>
        </Box>
      </form>

      <Box mt={2}>
        <Button
          variant="outlined"
          color="secondary"
          onClick={() => navigate("/recuperar-senha")}
          fullWidth
        >
          Voltar para Reenviar Código
        </Button>
      </Box>
    </Box>
  );
};

export default PasswordResetSent;
