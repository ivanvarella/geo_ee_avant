import { useState } from "react";
import axios from "axios";

const UploadCurriculo = () => {
  const [tituloCurriculo, setTituloCurriculo] = useState("");
  const [usuario, setUsuario] = useState(2); // Exemplo fixo; ajuste conforme necessário
  const [arquivo, setArquivo] = useState(null);

  const handleFileChange = (event) => {
    setArquivo(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append("titulo_curriculo", tituloCurriculo);
    formData.append("usuario", usuario);
    formData.append("arquivo", arquivo);

    try {
      const response = await axios.post(
        "http://localhost:8000/api/v1/curriculos/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      console.log("Currículo enviado com sucesso:", response.data);
    } catch (error) {
      console.error("Erro ao enviar currículo:", error.response.data);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Título do Currículo:</label>
        <input
          type="text"
          value={tituloCurriculo}
          onChange={(e) => setTituloCurriculo(e.target.value)}
          required
        />
      </div>
      <div>
        <label>Arquivo:</label>
        <input type="file" onChange={handleFileChange} required />
      </div>
      <button type="submit">Enviar Currículo</button>
    </form>
  );
};

export default UploadCurriculo;
