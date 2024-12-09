import { AppBar, Toolbar, Button, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import PropTypes from "prop-types";
import { useLogout } from "../../services/utils"; // Importando o hook useLogout

const MenuTopo = ({
  showSair = true,
  showLogin = true,
  showPerfil = true,
  showVagas = true,
  showCadastroCandidato = true,
  showCandidatoDetalhes = true,
  showCadastroResponsavel = true,
  showSenhaRequest = false,
  showSenhaSent = false,
  showSenhaComplete = false,
  showVerifyEmail = false,
  showVerificationRequest = false,
}) => {
  const navigate = useNavigate();
  const logout = useLogout(); // Usando o hook useLogout

  const handleNavigation = (route) => {
    navigate(route);
  };

  const handleLogout = () => {
    logout("/"); // Usando a função de logout do hook
  };

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          Avant
        </Typography>
        {showSair && (
          <Button color="inherit" onClick={() => handleLogout()}>
            Sair
          </Button>
        )}
        {showLogin && (
          <Button color="inherit" onClick={() => handleNavigation("/login")}>
            Login
          </Button>
        )}
        {showPerfil && (
          <Button color="inherit" onClick={() => handleNavigation("/perfil")}>
            Perfil
          </Button>
        )}
        {showVagas && (
          <Button color="inherit" onClick={() => handleNavigation("/vagas")}>
            Vagas
          </Button>
        )}
        {showCadastroCandidato && (
          <Button
            color="inherit"
            onClick={() => handleNavigation("/cadastro/candidato")}
          >
            Cadastro Candidato
          </Button>
        )}
        {showCandidatoDetalhes && (
          <Button
            color="inherit"
            onClick={() => handleNavigation("/candidato-detalhes")}
          >
            Candidato Detalhes
          </Button>
        )}
        {showCadastroResponsavel && (
          <Button
            color="inherit"
            onClick={() => handleNavigation("/cadastro/responsavel")}
          >
            Cadastro Empresa
          </Button>
        )}
        {showVerificationRequest && (
          <Button
            color="inherit"
            onClick={() => handleNavigation("/requisitar-verificacao")}
          >
            Requisitar Verificação de Email
          </Button>
        )}
        {showVerifyEmail && (
          <Button
            color="inherit"
            onClick={() => handleNavigation("/verificar-email")}
          >
            Verificar Email
          </Button>
        )}
        {showSenhaRequest && (
          <Button
            color="inherit"
            onClick={() => handleNavigation("/recuperar-senha")}
          >
            Recuperar Senha
          </Button>
        )}
        {showSenhaSent && (
          <Button
            color="inherit"
            onClick={() => handleNavigation("/recuperar-senha-enviado")}
          >
            Senha Enviado
          </Button>
        )}
        {showSenhaComplete && (
          <Button
            color="inherit"
            onClick={() => handleNavigation("/recuperar-senha-completo")}
          >
            Senha Completo
          </Button>
        )}
      </Toolbar>
    </AppBar>
  );
};

// Definição de tipos para as props
MenuTopo.propTypes = {
  showCadastroCandidato: PropTypes.bool,
  showCadastroResponsavel: PropTypes.bool,
  showSair: PropTypes.bool,
  showPerfil: PropTypes.bool,
  showVagas: PropTypes.bool,
  showLogin: PropTypes.bool,
  showSenhaRequest: PropTypes.bool,
  showSenhaSent: PropTypes.bool,
  showSenhaComplete: PropTypes.bool,
  showVerifyEmail: PropTypes.bool,
  showVerificationRequest: PropTypes.bool,
  showCandidatoDetalhes: PropTypes.bool,
};

export default MenuTopo;
