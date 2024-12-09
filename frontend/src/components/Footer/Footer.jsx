import { Box, Container, Grid, Typography, Link, useTheme } from "@mui/material";

const Footer = () => {
  const theme = useTheme();

  return (
    <Box
      sx={{
        bgcolor: theme.palette.primary.main,
        color: theme.palette.primary.contrastText,
        py: 4,
        boxShadow: "0 -4px 10px rgba(0, 0, 0, 0.2)",
        mt: "auto",
        width: "100%",
      }}
    >
      <Container maxWidth="lg">
        <Grid container spacing={4}>
          {/* INSTITUCIONAL */}
          <Grid item xs={12} sm={6} md={3}>
            <Typography variant="h6" gutterBottom>
              INSTITUCIONAL
            </Typography>
            <ul style={{ listStyle: "none", padding: 0 }}>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Avant Estágios
                </Link>
              </li>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Contato
                </Link>
              </li>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Política de Privacidade
                </Link>
              </li>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Política de Tratamento de Dados
                </Link>
              </li>
            </ul>
          </Grid>

          {/* PORTAL DO CANDIDATO */}
          <Grid item xs={12} sm={6} md={3}>
            <Typography variant="h6" gutterBottom>
              PORTAL DO CANDIDATO
            </Typography>
            <ul style={{ listStyle: "none", padding: 0 }}>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Cadastro de Estudantes
                </Link>
              </li>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Vagas de Estágio
                </Link>
              </li>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Regulamentação
                </Link>
              </li>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Processos Seletivos
                </Link>
              </li>
            </ul>
          </Grid>

          {/* PORTAL DA EMPRESA */}
          <Grid item xs={12} sm={6} md={3}>
            <Typography variant="h6" gutterBottom>
              PORTAL DA EMPRESA
            </Typography>
            <ul style={{ listStyle: "none", padding: 0 }}>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Cadastro de Empresa
                </Link>
              </li>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Contratação de Estagiários
                </Link>
              </li>
            </ul>
          </Grid>

          {/* PORTAL DA INSTITUIÇÃO */}
          <Grid item xs={12} sm={6} md={3}>
            <Typography variant="h6" gutterBottom>
              PORTAL DA INSTITUIÇÃO
            </Typography>
            <ul style={{ listStyle: "none", padding: 0 }}>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Empregabilidade
                </Link>
              </li>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Cadastro de Vagas
                </Link>
              </li>
              <li>
                <Link href="#" color="inherit" underline="hover">
                  Contato
                </Link>
              </li>
            </ul>
          </Grid>
        </Grid>

        <Box sx={{ textAlign: "center", marginTop: "40px" }}>
          <Typography variant="body2" color="inherit">
            COPYRIGHT © 2024 - Avant GEO - EE
          </Typography>
        </Box>
      </Container>
    </Box>
  );
};

export default Footer;
