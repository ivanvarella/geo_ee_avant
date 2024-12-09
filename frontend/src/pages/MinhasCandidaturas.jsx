import { useState } from "react";
import {
  Container,
  TextField,
  Typography,
  Card,
  CardContent,
  MenuItem,
  Select,
  FormControl,
  InputLabel,
  Box,
} from "@mui/material";
import Grid from "@mui/material/Grid2";

const MinhasCandidaturas = () => {
  // Dados fictícios para exemplo
  const candidaturas = [
    {
      nome: "Estágio em Engenharia",
      empresa: "Tech Solutions",
      setor: "Engenharia",
      expiracao: "15/12/2024",
      modalidade: "Presencial",
    },
    {
      nome: "Desenvolvedor Frontend",
      empresa: "CodeFactory",
      setor: "Soluções de Software",
      expiracao: "20/12/2024",
      modalidade: "À distância",
    },
    {
      nome: "Assistente de Marketing",
      empresa: "MarketPro",
      setor: "Marketing",
      expiracao: "25/12/2024",
      modalidade: "Presencial",
    },
    {
      nome: "Designer Gráfico",
      empresa: "DesignCo",
      setor: "Design Gráfico",
      expiracao: "01/01/2025",
      modalidade: "À distância",
    },
  ];

  const [busca, setBusca] = useState("");
  const [filtroEmpresa, setFiltroEmpresa] = useState("");
  const [filtroModalidade, setFiltroModalidade] = useState("");

  // Filtrar candidaturas com base no campo de busca e filtros adicionais
  const vagasFiltradas = candidaturas.filter((vaga) => {
    const nomeMatch = vaga.nome.toLowerCase().includes(busca.toLowerCase());
    const empresaMatch = filtroEmpresa ? vaga.empresa === filtroEmpresa : true;
    const modalidadeMatch = filtroModalidade
      ? vaga.modalidade === filtroModalidade
      : true;

    return nomeMatch && empresaMatch && modalidadeMatch;
  });

  // Obter lista única de empresas para o filtro
  const empresasDisponiveis = [
    ...new Set(candidaturas.map((vaga) => vaga.empresa)),
  ];

  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Minhas Candidaturas
      </Typography>

      {/* Campos de filtro */}
      <Box display="flex" gap={2} alignItems="center" sx={{ mb: 3 }}>
        <TextField
          fullWidth
          variant="outlined"
          label="Buscar vaga pelo nome"
          value={busca}
          onChange={(e) => setBusca(e.target.value)}
        />

        <FormControl sx={{ minWidth: 180 }}>
          <InputLabel>Empresa</InputLabel>
          <Select
            value={filtroEmpresa}
            onChange={(e) => setFiltroEmpresa(e.target.value)}
            label="Empresa"
          >
            <MenuItem value="">Todas</MenuItem>
            {empresasDisponiveis.map((empresa, index) => (
              <MenuItem key={index} value={empresa}>
                {empresa}
              </MenuItem>
            ))}
          </Select>
        </FormControl>

        <FormControl sx={{ minWidth: 180 }}>
          <InputLabel>Modalidade</InputLabel>
          <Select
            value={filtroModalidade}
            onChange={(e) => setFiltroModalidade(e.target.value)}
            label="Modalidade"
          >
            <MenuItem value="">Todas</MenuItem>
            <MenuItem value="Presencial">Presencial</MenuItem>
            <MenuItem value="À distância">À distância</MenuItem>
          </Select>
        </FormControl>
      </Box>

      {/* Exibição de vagas */}
      <Grid container spacing={2}>
        {vagasFiltradas.length > 0 ? (
          vagasFiltradas.map((vaga, index) => (
            <Grid item xs={12} sm={6} md={4} key={index}>
              <Card sx={{ height: "100%" }}>
                <CardContent>
                  <Typography variant="h6" color="primary">
                    {vaga.nome}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Empresa: {vaga.empresa}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Setor: {vaga.setor}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Expira em: {vaga.expiracao}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Modalidade: {vaga.modalidade}
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          ))
        ) : (
          <Typography variant="body1" sx={{ mt: 3 }}>
            Nenhuma vaga encontrada.
          </Typography>
        )}
      </Grid>
    </Container>
  );
};

export default MinhasCandidaturas;
