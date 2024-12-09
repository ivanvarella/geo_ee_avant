import PropTypes from "prop-types";
import { Navigate } from "react-router-dom";
import { isLoggedIn } from "../../services/utils";

const ProtectedRoute = ({ children }) => {
  if (!isLoggedIn()) {
    // Se o usuário não está logado, redirecione para o login
    return <Navigate to="/login" replace />;
  }

  // Caso esteja autenticado, renderize o componente filho
  return children;
};

// Validando os props com PropTypes
ProtectedRoute.propTypes = {
  children: PropTypes.node.isRequired, // children é um nó React obrigatório
};

export default ProtectedRoute;
