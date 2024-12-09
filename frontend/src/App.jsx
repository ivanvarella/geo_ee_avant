import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import AuthLayout from "./layouts/AuthLayout";
import MainLayout from "./layouts/MainLayout";
import {
  Home,
  Login,
  CadastroUser,
  CandidatoDetalhes,
  CadastroEmpresa,
  CandidatoProfile,
  Vagas,
  PasswordResetRequest,
  PasswordResetSent,
  PasswordResetComplete,
  VerifyEmail,
  VerificationRequest,
} from "./pages";
import ProtectedRoute from "./components/ProtectedRoute/ProtectedRoute";
import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        {/* AuthLayout como wrapper para a página de Login */}
        <Route element={<AuthLayout />}>
          <Route path="/Login" element={<Login />} />
          <Route
            path="/cadastro/candidato"
            element={<CadastroUser tipo="candidato" />}
          />
          <Route
            path="/cadastro/responsavel"
            element={<CadastroUser tipo="responsavel" />}
          />
          <Route path="/verificar-email" element={<VerifyEmail />} />
          <Route
            path="/requisitar-verificacao"
            element={<VerificationRequest />}
          />
          <Route path="/recuperar-senha" element={<PasswordResetRequest />} />
          <Route
            path="/recuperar-senha-enviado"
            element={<PasswordResetSent />}
          />
          <Route
            path="/recuperar-senha-completo"
            element={<PasswordResetComplete />}
          />
        </Route>

        {/* MainLayout como wrapper para páginas protegidas */}
        <Route element={<MainLayout />}>
          <Route path="/" element={<Home />} />
          <Route path="/empresa" element={<CadastroEmpresa />} />
          <Route
            path="/candidato-detalhes"
            element={
              <ProtectedRoute>
                <CandidatoDetalhes />
              </ProtectedRoute>
            }
          />
          <Route
            path="/perfil"
            element={
              <ProtectedRoute>
                <CandidatoProfile />
              </ProtectedRoute>
            }
          />
          <Route path="/vagas" element={<Vagas />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
