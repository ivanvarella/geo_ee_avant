import { Card, CardContent, Typography, useTheme } from "@mui/material";
import Grid from "@mui/material/Grid2";

const CandidatoProfile = ({ nome, email, cpf, tipoUsuario, usuarioDesde }) => {
  const theme = useTheme();

  return (
    <Card
      sx={{
        maxWidth: 600,
        margin: "20px auto",
        padding: theme.spacing(2),
        boxShadow: "0 4px 10px rgba(0, 0, 0, 0.1)",
      }}
    >
      <CardContent>
        <Typography variant="h5" color="primary" gutterBottom>
          Perfil do Usuário
        </Typography>

        <Grid container spacing={2}>
          <Grid item xs={12}>
            <Typography variant="subtitle1" fontWeight="bold">
              Nome:
            </Typography>
            <Typography variant="body1">{nome}</Typography>
          </Grid>

          <Grid item xs={12}>
            <Typography variant="subtitle1" fontWeight="bold">
              E-mail:
            </Typography>
            <Typography variant="body1">{email}</Typography>
          </Grid>

          <Grid item xs={12}>
            <Typography variant="subtitle1" fontWeight="bold">
              CPF:
            </Typography>
            <Typography variant="body1">{cpf}</Typography>
          </Grid>

          <Grid item xs={12}>
            <Typography variant="subtitle1" fontWeight="bold">
              Tipo de Usuário:
            </Typography>
            <Typography variant="body1">{tipoUsuario}</Typography>
          </Grid>

          <Grid item xs={12}>
            <Typography variant="subtitle1" fontWeight="bold">
              Usuário desde:
            </Typography>
            <Typography variant="body1">{usuarioDesde}</Typography>
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );
};

export default CandidatoProfile;
