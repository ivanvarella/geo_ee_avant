import axios from "axios";
import { useNavigate } from "react-router-dom";

export const getAccessToken = () => {
  return localStorage.getItem("access_token");
};

export const getRefreshToken = () => {
  return localStorage.getItem("refresh_token");
};

export const isLoggedIn = () => {
  return !!getAccessToken();
};

export const useLogout = () => {
  const navigate = useNavigate();

  const logout = (redirectTo = "/") => {
    const refreshToken = getRefreshToken();
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("user_email");

    // Invalidar o refresh token no backend
    axios
      .post("http://127.0.0.1:8000/api/v1/token/blacklist/", {
        refresh: refreshToken,
      })
      .catch((error) => {
        console.error("Erro ao invalidar o token:", error);
      });

    navigate(redirectTo);
  };

  return logout;
};
