import { Outlet } from "react-router-dom";
import MenuTopo from "../components/Header/Header";
import Footer from "../components/Footer/Footer";
import { Box, Container } from "@mui/material";

const AuthLayout = () => {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        minHeight: "100vh",
      }}
    >
      <MenuTopo showHome={false} showPerfil={false} showVagas={true} />
      <Container
        sx={{
          flexGrow: 1,
        }}
      >
        <Outlet />
      </Container>
      <Footer />
    </Box>
  );
};

export default AuthLayout;
