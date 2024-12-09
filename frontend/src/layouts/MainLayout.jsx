import { Outlet } from "react-router-dom";
import PropTypes from "prop-types";
import MenuTopo from "../components/Header/Header";
import Footer from "../components/Footer/Footer";
import { Box, Container } from "@mui/material";

const MainLayout = () => {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        minHeight: "100vh", // Ocupa toda a altura da tela
      }}
    >
      <MenuTopo
        showSair={true}
        showPerfil={true}
        showVagas={true}
        showCadastroCandidato={true}
        showCadastroResponsavel={true}
      />

      <Container
        sx={{
          flexGrow: 1, // Faz o conteúdo crescer e ocupar o espaço restante
        }}
      >
        <Outlet />
      </Container>

      <Footer />
    </Box>
  );
};

// Definindo a validação de 'children'
MainLayout.propTypes = {
  children: PropTypes.node,
};

export default MainLayout;
