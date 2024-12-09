import { useState } from "react";
import {
  Box,
  Card,
  CardContent,
  Typography,
  TextField,
  Select,
  MenuItem,
  InputLabel,
  FormControl,
} from "@mui/material";
import Grid from "@mui/material/Grid2";

const vagasDisponiveis = [
  {
    nome: "Estágio em Engenharia Civil",
    setor: "Engenharia",
    expiracao: "15/12/2024",
  },
  {
    nome: "Desenvolvedor Frontend",
    setor: "Soluções de Software",
    expiracao: "20/12/2024",
  },
  {
    nome: "Estágio em Direito",
    setor: "Escritório de Direito",
    expiracao: "05/01/2025",
  },
  {
    nome: "Analista Financeiro Júnior",
    setor: "Consultoria Financeira",
    expiracao: "10/01/2025",
  },
  {
    nome: "Estágio em Marketing Digital",
    setor: "Marketing",
    expiracao: "15/01/2025",
  },
  {
    nome: "Assistente de Enfermagem",
    setor: "Saúde e Medicina",
    expiracao: "25/12/2024",
  },
  { nome: "Professor Assistente", setor: "Educação", expiracao: "30/12/2024" },
  { nome: "Estágio em Logística", setor: "Logística", expiracao: "10/02/2025" },
  {
    nome: "Recrutador Júnior",
    setor: "Recursos Humanos",
    expiracao: "05/02/2025",
  },
  {
    nome: "Designer Gráfico",
    setor: "Design Gráfico",
    expiracao: "20/02/2025",
  },
];

const Vagas = () => {
  const [search, setSearch] = useState("");
  const [setor, setSetor] = useState("");

  // Função para filtrar vagas
  const vagasFiltradas = vagasDisponiveis.filter((vaga) => {
    const nomeMatch = vaga.nome.toLowerCase().includes(search.toLowerCase());
    const setorMatch = setor === "" || vaga.setor === setor;
    return nomeMatch && setorMatch;
  });

  return (
    <Box sx={{ padding: 4 }}>
      <Typography variant="h4" color="primary" gutterBottom>
        Vagas de Estágio
      </Typography>

      {/* Campo de pesquisa */}
      <Grid container spacing={2} sx={{ marginBottom: 2 }}>
        <Grid item xs={12} md={6}>
          <TextField
            fullWidth
            label="Pesquisar vaga"
            variant="outlined"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </Grid>

        {/* Filtro de setor */}
        <Grid item xs={12} md={6}>
          <FormControl fullWidth>
            <InputLabel>Filtrar por setor</InputLabel>
            <Select
              value={setor}
              onChange={(e) => setSetor(e.target.value)}
              label="Filtrar por setor"
            >
              <MenuItem value="">Todos</MenuItem>
              <MenuItem value="Engenharia">Engenharia</MenuItem>
              <MenuItem value="Soluções de Software">
                Soluções de Software
              </MenuItem>
              <MenuItem value="Escritório de Direito">
                Escritório de Direito
              </MenuItem>
              <MenuItem value="Consultoria Financeira">
                Consultoria Financeira
              </MenuItem>
              <MenuItem value="Marketing">Marketing</MenuItem>
              <MenuItem value="Saúde e Medicina">Saúde e Medicina</MenuItem>
              <MenuItem value="Educação">Educação</MenuItem>
              <MenuItem value="Logística">Logística</MenuItem>
              <MenuItem value="Recursos Humanos">Recursos Humanos</MenuItem>
              <MenuItem value="Design Gráfico">Design Gráfico</MenuItem>
            </Select>
          </FormControl>
        </Grid>
      </Grid>

      {/* Lista de vagas */}
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
                    Setor: {vaga.setor}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Expira em: {vaga.expiracao}
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          ))
        ) : (
          <Typography
            variant="body1"
            color="text.secondary"
            sx={{ marginTop: 2 }}
          >
            Nenhuma vaga encontrada.
          </Typography>
        )}
      </Grid>
    </Box>
  );
};

export default Vagas;
