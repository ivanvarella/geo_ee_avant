import { Typography, Button } from "@mui/material";
import { Link } from "react-router-dom";

const PasswordResetComplete = () => {
  return (
    <div>
      <Typography variant="h5">Senha redefinida com sucesso</Typography>
      <Typography>Você pode agora fazer login com sua nova senha.</Typography>
      <Link to="/login">
        <Button variant="contained" color="primary">
          Ir para o Login
        </Button>
      </Link>
    </div>
  );
};

export default PasswordResetComplete;
