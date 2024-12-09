import {
  Box,
  CssBaseline,
  Drawer,
  Toolbar,
  List,
  ListItem,
  ListItemButton,
  ListItemText,
  ListItemIcon,
  Typography,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import { useLogout } from "../../services/utils";

// Ícones do Material UI
import HomeIcon from "@mui/icons-material/Home"; // Ícone para 'Início'
import SearchIcon from "@mui/icons-material/Search"; // Ícone para 'Busca de vagas'
import ExitToAppIcon from "@mui/icons-material/ExitToApp"; // Ícone para 'Sair'

export const drawerWidth = 240; // Exportação da constante

const MenuLateral = () => {
  const navigate = useNavigate();
  const logout = useLogout();

  const handleLogout = () => {
    logout("/"); // Usando a função de logout do hook
  };

  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      {/* Drawer Persistente */}
      <Drawer
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          "& .MuiDrawer-paper": {
            width: drawerWidth,
            boxSizing: "border-box",
            top: "64px", // Altura do Header (ajuste conforme necessário)
            bottom: "260px", // Altura do Footer (ajuste conforme necessário)
            zIndex: -1,
          },
        }}
        variant="permanent"
        anchor="left"
      >
        <Toolbar>
          <Typography variant="h6" noWrap>
            Menu
          </Typography>
        </Toolbar>
        <List>
          {/* Botão 'Início' */}
          <ListItem disablePadding>
            <ListItemButton onClick={() => navigate("/")}>
              <ListItemIcon>
                <HomeIcon color="primary" /> {/* Ícone para 'Início' */}
              </ListItemIcon>
              <ListItemText primary="Início" />
            </ListItemButton>
          </ListItem>
          {/* Botão 'Busca de vagas' */}
          <ListItem disablePadding>
            <ListItemButton onClick={() => navigate("/vagas")}>
              <ListItemIcon>
                <SearchIcon color="primary" />{" "}
                {/* Ícone para 'Busca de vagas' */}
              </ListItemIcon>
              <ListItemText primary="Busca de vagas" />
            </ListItemButton>
          </ListItem>
          {/* Botão 'Sair' */}
          <ListItem disablePadding>
            <ListItemButton onClick={handleLogout}>
              <ListItemIcon>
                <ExitToAppIcon color="error" /> {/* Ícone para 'Sair' */}
              </ListItemIcon>
              <ListItemText primary="Sair" />
            </ListItemButton>
          </ListItem>
        </List>
      </Drawer>
    </Box>
  );
};

export default MenuLateral;
