import { useState, useEffect } from "react";
import PropTypes from "prop-types";
import {
  Box,
  CircularProgress,
  Container,
  Typography,
  Card,
  CardContent,
} from "@mui/material";
import { makeApiCall } from "../../services/api"; // Importando a função makeApiCall
import { getAccessToken } from "../../services/utils"; // Importando a função getAccessToken

const UserProfile = () => {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const accessToken = getAccessToken(); // Obtém o token de acesso

        if (!accessToken) {
          throw new Error("Token de acesso não encontrado.");
        }

        const response = await makeApiCall("candidato/", {}, "GET"); // Faz a chamada usando makeApiCall

        if (response && response.results && response.results.length > 0) {
          setUserData(response.results[0]); // Supondo que os dados do usuário estejam no primeiro item da lista
        } else {
          throw new Error("Dados do usuário não encontrados.");
        }
      } catch (err) {
        console.error("Erro ao buscar dados do usuário:", err);
        setError("Erro ao carregar dados do usuário.");
      } finally {
        setLoading(false);
      }
    };

    fetchUserData();
  }, []);

  if (loading)
    return (
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        minHeight="100vh"
      >
        <CircularProgress />
      </Box>
    );

  if (error)
    return (
      <Typography variant="body1" color="error" align="center">
        {error}
      </Typography>
    );

  return (
    <Container>
      <Typography variant="h5" align="center" gutterBottom>
        Dados do Usuário
      </Typography>
      <Card variant="outlined">
        <CardContent>
          <Typography variant="h5">
            {userData.first_name} {userData.last_name}
          </Typography>
          <Typography variant="body1">
            <strong>Id:</strong> {userData.id}
          </Typography>
          <Typography variant="body1">
            <strong>Username:</strong> {userData.username}
          </Typography>
          <Typography variant="body1">
            <strong>Email:</strong> {userData.email}
          </Typography>
          <Typography variant="body1">
            <strong>CPF:</strong> {userData.cpf}
          </Typography>
          <Typography variant="body1">
            <strong>Data de Nascimento:</strong> {userData.data_nascimento}
          </Typography>
          <Typography variant="body1">
            <strong>Ativo:</strong> {userData.is_active ? "Sim" : "Não"}
          </Typography>
          <Typography variant="body1">
            <strong>Tipo:</strong> {userData.tipo}
          </Typography>
        </CardContent>
      </Card>
    </Container>
  );
};

UserProfile.propTypes = {
  accessToken: PropTypes.string.isRequired, // Esse prop agora não é mais necessário
};

export default UserProfile;
