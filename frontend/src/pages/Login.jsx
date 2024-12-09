import { useState, useEffect } from "react";
import { useNavigate, useLocation } from "react-router-dom"; // useNavigate para navegação e useLocation para pegar o estado de navegação
import { makeApiCall } from "../services/api"; // Importando a função makeApiCall para realizar as requisições API
import {
  Container,
  Box,
  Typography,
  TextField,
  Button,
  Alert,
  Link,
} from "@mui/material"; // Componentes do MUI para layout e exibição
import { isLoggedIn, useLogout } from "../services/utils";

const Login = () => {
  const [email, setEmail] = useState(""); // Estado para armazenar o email do usuário
  const [password, setPassword] = useState(""); // Estado para armazenar a senha do usuário
  const [error, setError] = useState(""); // Estado para armazenar mensagens de erro
  const [successMessages, setSuccessMessages] = useState([]); // Usando um array para armazenar múltiplas mensagens de sucesso

  const navigate = useNavigate(); // Hook para navegação entre páginas
  const location = useLocation(); // Hook para acessar o estado de navegação da URL
  const logout = useLogout(); // Usando a função de logout

  // useEffect para verificar se há mensagens de sucesso vindo da página de cadastro
  useEffect(() => {
    if (location.state?.messages) {
      const { cadastro, emailVerification, emailVerificationDone } =
        location.state.messages;

      // Cria um array com todas as mensagens de sucesso
      const newMessages = [];
      if (cadastro) newMessages.push(cadastro); // Adiciona a mensagem de cadastro
      if (emailVerification) newMessages.push(emailVerification); // Adiciona a mensagem de verificação de e-mail
      if (emailVerificationDone) newMessages.push(emailVerificationDone);

      setSuccessMessages(newMessages); // Atualiza o estado com as novas mensagens
    }
  }, [location.state]);

  // useEffect para limpar a mensagem de sucesso após interação do usuário
  useEffect(() => {
    // Função que será chamada quando o usuário tentar logar ou navegar
    const clearSuccessMessage = () => {
      successMessages([]); // Limpa a mensagens de sucesso
    };

    // Se a mensagem de sucesso existir, configura a limpeza após o primeiro evento
    if (successMessages) {
      const timer = setTimeout(clearSuccessMessage, 2500); // Limpa após a interação (delay de 2500ms)

      return () => clearTimeout(timer); // Limpa o timer caso o componente seja desmontado ou o efeito seja re-executado
    }
  }, [successMessages]);

  const handleLogin = async (e) => {
    e.preventDefault(); // Impede o comportamento padrão do formulário (recarregar a página)
    setError(""); // Limpa qualquer erro anterior

    try {
      // Realiza a chamada da API para autenticação com os dados de email e senha
      const response = await makeApiCall("token/", { email, password }, "POST");

      // Verifica se os tokens (access e refresh) estão na resposta da API
      if (response.access && response.refresh) {
        // Se os tokens forem encontrados, armazena-os no localStorage
        localStorage.setItem("access_token", response.access);
        localStorage.setItem("refresh_token", response.refresh);
        localStorage.setItem("user_email", email); // Armazena também o email do usuário
        navigate("/"); // Redireciona para a página inicial após o login bem-sucedido
      } else {
        // Caso os tokens não sejam encontrados na resposta, exibe um erro
        setError("Tokens não encontrados na resposta.");
      }
    } catch (err) {
      // Caso ocorra algum erro na requisição, exibe o erro
      console.error(
        "Erro ao fazer login:",
        err.response ? err.response.data : err.message
      );
      setError("Erro ao fazer login. Verifique suas credenciais.");
    }
  };

  return (
    <Container component="main" maxWidth="xs">
      <Typography variant="h3" component="h2" textAlign="center" gutterBottom>
        Seja bem-vindo
      </Typography>

      <Box sx={{ display: "flex", flexDirection: "column", alignItems: "center", marginTop: 8, padding: 3, borderRadius: 2, boxShadow: 3 }}>
        {isLoggedIn() ? (
          <>
            <Typography variant="h5" component="h2" textAlign="center" gutterBottom>
              Você já está logado!
            </Typography>
            <Button
              variant="contained"
              color="secondary"
              fullWidth
              sx={{ marginTop: 2 }}
              onClick={() => logout("/")} // Realiza o logout e redireciona para a página inicial
            >
              Sair
            </Button>
          </>
        ) : (
          <>
            <Typography variant="h5" component="h2" textAlign="center" gutterBottom>
              Login
            </Typography>

            {/* Exibe as mensagens de sucesso vindas da página de cadastro */}
            {successMessages.length > 0 && (
              <Box sx={{ width: "100%", marginTop: 2 }}>
                {successMessages.map((message, index) => (
                  <Alert key={index} severity="success" sx={{ marginBottom: 1 }}>
                    {message}
                  </Alert>
                ))}
              </Box>
            )}

            {/* Exibe o erro de login, caso haja */}
            {error && (
              <Alert severity="error" sx={{ width: "100%", marginTop: 2 }}>
                {error}
              </Alert>
            )}

            <form onSubmit={handleLogin} style={{ width: "100%" }}>
              <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email"
                placeholder="Digite seu email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                autoComplete="email"
                autoFocus
              />
              <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                id="password"
                label="Senha"
                type="password"
                placeholder="Digite sua senha"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                autoComplete="current-password"
              />
              <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth
                sx={{ marginTop: 2 }}
              >
                Entrar
              </Button>
            </form>
            <Box sx={{ marginTop: 2 }}>
              <Link href="/recuperar-senha" variant="body2" sx={{ display: "block", textAlign: "center", marginTop: 1 }}>
                Esqueceu sua senha? Clique aqui para redefinir.
              </Link>
            </Box>
          </>
        )}
      </Box>
    </Container>
  );
};

export default Login;
