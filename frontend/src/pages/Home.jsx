import { Box, Container, Typography, Paper } from "@mui/material";

const Home = () => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      {/* Título principal da página */}
      <Typography variant="h3" component="h1" gutterBottom align="center">
        Bem-vindo ao Avant.
      </Typography>

      {/* Descrição do sistema */}
      <Typography variant="h6" paragraph align="center">
        O Avant é um sistema de estágios que conecta candidatos e
        empresas. Empresas podem cadastrar vagas de estágio e
        candidatos podem se inscrever para essas vagas.
      </Typography>

      {/* Seções de informações */}
      <Box sx={{ display: "flex", flexWrap: "wrap", gap: 4 }}>
        {/* Seção sobre as empresas */}
        <Box sx={{ flex: "1 1 100%", md: "1 1 48%" }}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h5" component="h2" gutterBottom>
              Empresas
            </Typography>
            <Typography variant="body1">
              Cadastre vagas de estágio, visualize
              candidatos interessados e gerencie o recrutamento de estagiários do início ao fim. Cadastre-se agora e encontre os talentos de que
              você precisa para a sua empresa.
            </Typography>
          </Paper>
        </Box>

        {/* Seção sobre os candidatos */}
        <Box sx={{ flex: "1 1 100%", md: "1 1 48%" }}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h5" component="h2" gutterBottom>
              Candidatos
            </Typography>
            <Typography variant="body1">
              Visualize as vagas de estágio disponíveis, candidate-se
              para aquelas que mais se encaixam no seu perfil e acompanhe o status da sua inscrição.
              Cadastre-se para começar sua brilhante jornada profissional.
            </Typography>
          </Paper>
        </Box>
      </Box>

      {/* Chamada para ação */}
      <Box sx={{ mt: 5, textAlign: "center" }}>
        <Typography variant="h6" paragraph>
          Entre em contato com o suporte para mais informações ou registre-se
          agora!
        </Typography>
        {/* Aqui você pode adicionar um botão ou link para as páginas de cadastro ou login */}
      </Box>
    </Container>
  );
};

export default Home;
