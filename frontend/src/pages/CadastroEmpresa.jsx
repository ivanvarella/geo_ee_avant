import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  Container,
  TextField,
  Button,
  Typography,
  Alert,
  Box,
  MenuItem,
  FormControl,
  InputLabel,
  Select,
} from "@mui/material";
import { makeApiCall } from "../services/api"; // Importando makeApiCall

const CadastroEmpresa = () => {
  const [apiResponse, setApiResponse] = useState("");
  const [errorRequest, setErrorRequest] = useState(false);
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    cpf: "",
    data_nascimento: "",
    area_atuacao: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    makeApiCallCandidato("candidato/", formData);
  };

  const makeApiCallCandidato = async (endpoint, data) => {
    try {
      const response = await makeApiCall(endpoint, data); // Usando makeApiCall de api.js
      setApiResponse(JSON.stringify(response, null, 2));
      setErrorRequest(false);
    } catch (error) {
      console.error("Erro ao fazer a chamada à API:", error);
      if (error.response) {
        setErrorRequest(true);
      }
    }
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" component="h1" gutterBottom>
        Empresa
      </Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Nome"
          variant="outlined"
          fullWidth
          margin="normal"
          name="first_name"
          value={formData.first_name}
          onChange={handleChange}
          required
        />
        <FormControl fullWidth margin="normal" required>
          <InputLabel id="area-atuacao-label">Segmento da empresa</InputLabel>
          <Select
            labelId="area-atuacao-label"
            id="area-atuacao"
            name="area_atuacao"
            value={formData.area_atuacao} // Isso agora terá um valor inicial válido
            onChange={handleChange}
            label="Segmento da empresa"
            required
          >
            <MenuItem value="engenharia">Engenharia</MenuItem>
            <MenuItem value="solucoes_software">Soluções de Software</MenuItem>
            <MenuItem value="escritorio_direito">
              Escritório de Direito
            </MenuItem>
            <MenuItem value="consultoria_financeira">
              Consultoria Financeira
            </MenuItem>
            <MenuItem value="marketing">Marketing</MenuItem>
            <MenuItem value="saude_medicina">Saúde e Medicina</MenuItem>
            <MenuItem value="educacao">Educação</MenuItem>
            <MenuItem value="logistica">Logística</MenuItem>
            <MenuItem value="recursos_humanos">Recursos Humanos</MenuItem>
            <MenuItem value="design_grafico">Design Gráfico</MenuItem>
          </Select>
        </FormControl>
        <TextField
          label="E-mail corporativo"
          variant="outlined"
          fullWidth
          margin="normal"
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <TextField
          label="Senha"
          variant="outlined"
          fullWidth
          margin="normal"
          type="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <TextField
          label="CNPJ"
          variant="outlined"
          fullWidth
          margin="normal"
          name="cnpj"
          value={formData.CNPJ}
          onChange={handleChange}
          required
        />

        <Box mt={2}>
          <Button variant="contained" color="primary" type="submit" fullWidth>
            Registrar
          </Button>
        </Box>
      </form>
      <Box mt={2}>
        <Button
          variant="outlined"
          color="primary"
          onClick={() => navigate("/api-test")}
          fullWidth
        >
          Voltar
        </Button>
      </Box>
      {apiResponse && (
        <Alert
          severity={errorRequest ? "error" : "info"}
          style={{ marginTop: "16px" }}
        >
          {apiResponse}
        </Alert>
      )}
    </Container>
  );
};

export default CadastroEmpresa;
