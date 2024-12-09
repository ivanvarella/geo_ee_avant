import { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { makeApiCall, buscarEnderecoPorCep } from "../../services/api";
import {
  Container,
  TextField,
  Button,
  Typography,
  Alert,
  Box,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Checkbox,
  FormControlLabel,
  IconButton,
  Tooltip,
} from "@mui/material";
import AddIcon from "@mui/icons-material/Add";
import { useForm, useFieldArray } from "react-hook-form";
import IMask from "imask";
import Telefone from "../../components/Telefone/Telefone";
import { isLoggedIn } from "../../services/utils";
import { getResetData } from "./utils";

const CandidatoDetalhes = () => {
  // Estados para controle de mensagens e dados do formulário
  const [apiResponse, setApiResponse] = useState(""); // Armazena a resposta da API
  const [errorRequest, setErrorRequest] = useState(false); // Indica se houve erro na requisição
  const [isDeficiente, setIsDeficiente] = useState(false); // Controle para exibir campo de deficiência
  const [endereco, setEndereco] = useState({
    logradouro: "",
    bairro: "",
    localidade: "",
    uf: "",
    estado: "",
    regiao: "",
  }); // Armazena os dados do endereço com base no CEP

  const navigate = useNavigate(); // Navegação entre páginas
  const cepRef = useRef(null); // Referência para campo de CEP (para aplicar máscara)
  const hasFetched = useRef(false);

  // Configuração do formulário com react-hook-form
  const {
    register,
    handleSubmit,
    formState: { errors },
    control,
    setValue,
    watch,
    reset,
  } = useForm({
    defaultValues: {
      genero: "",
      tipo_deficiencia: "",
      linkedin: "",
      github: "",
      cep: "",
      numero: "",
      complemento: "",
      telefones: [], // Lista dinâmica para múltiplos telefones
    },
  });

  const { fields, append, remove } = useFieldArray({
    control,
    name: "telefones",
  });

  // Referência para os campos de telefone
  const phoneRefs = useRef([]);

  // Função para aplicar máscara no telefone baseado no tipo
  const applyPhoneMask = (element, tipo) => {
    if (!element) return;

    let maskPattern;
    switch (tipo) {
      case "celular":
        maskPattern = "(00) 00000-0000";
        break;
      case "residencial":
      case "comercial":
        maskPattern = "(00) 0000-0000";
        break;
      default:
        maskPattern = "(00) 00000-0000";
    }

    IMask(element, {
      mask: maskPattern,
      lazy: false,
      placeholderChar: "_",
    });
  };

  // Efeito para aplicar máscaras nos campos de telefone
  useEffect(() => {
    fields.forEach((field, index) => {
      if (phoneRefs.current[index]) {
        const tipo = watch(`telefones.${index}.tipo`);
        applyPhoneMask(phoneRefs.current[index], tipo);
      }
    });
  }, [fields, watch]);

  // Função para adicionar novo telefone
  const handleAddPhone = () => {
    if (fields.length >= 3) return; // Limita a 3 telefones
    append({
      tipo: "celular", // Valor padrão para evitar erro de undefined
      numero: "",
    });
  };

  // Função para remover telefone
  const handleRemovePhone = (index) => {
    remove(index);
  };

  const genero = watch("genero", ""); // Monitora alterações no campo "gênero"

  // Aplicação de máscara no campo de CEP
  useEffect(() => {
    if (cepRef.current) {
      IMask(cepRef.current, { mask: "00000-000" }); // Máscara para CEP
    }
  }, []);

  // Função para buscar endereço com base no CEP
  const buscarEndereco = async (cep) => {
    if (!cep) return; // Não busca se o CEP estiver vazio
    try {
      const response = await buscarEnderecoPorCep({ cep });
      if (response.erro) throw new Error("CEP não encontrado."); // Trata erro de CEP inválido
      // Atualiza o estado com os dados do endereço
      setEndereco({
        cep: response.cep,
        logradouro: response.logradouro,
        bairro: response.bairro,
        localidade: response.localidade,
        uf: response.uf,
        estado: response.estado,
        regiao: response.regiao,
      });

      // Popula automaticamente os campos do formulário com os dados do endereço
      setValue("cep", response.cep); // Preenche o campo CEP
      setValue("logradouro", response.logradouro); // Preenche o campo Logradouro
      setValue("bairro", response.bairro); // Preenche o campo Bairro
      setValue("localidade", response.localidade); // Preenche o campo Localidade
      setValue("uf", response.uf); // Preenche o campo UF
      setValue("estado", response.estado); // Preenche o campo Estado
      setValue("regiao", response.regiao); // Preenche o campo Regiao
    } catch (error) {
      console.error("Erro ao buscar endereço:", error.message);
      setEndereco({}); // Limpa o endereço em caso de erro
    }
  };

  // Atualiza o estado para exibição do campo de tipo de deficiência
  const handleDeficienteChange = (event) => {
    setIsDeficiente(event.target.checked);
  };

  // Função para garantir que a URL tenha http:// ou https:// no início
  const validarUrl = (url) => {
    // Verifica se a URL já começa com "http://" ou "https://"
    if (!url.startsWith("http://") && !url.startsWith("https://")) {
      // Se não começar com esses prefixos, adiciona "https://"
      return `https://${url}`;
    }
    return url; // Se já começar com http:// ou https://, retorna a URL como está
  };

  // Função chamada no envio do formulário
  const onSubmit = async (data) => {
    // Valida as URLs de LinkedIn e GitHub
    const linkedinValido = validarUrl(data.linkedin);
    const githubValido = validarUrl(data.github);

    // Separando os dados em suas respectivas categorias
    const dadosCandidato = {
      genero: data.genero,
      tipo_deficiencia: isDeficiente ? data.tipo_deficiencia : "", // Adiciona o tipo de deficiência apenas se for deficiente
      linkedin: linkedinValido,
      github: githubValido,
      deficiencia: isDeficiente,
    };

    const enderecos = {
      cep: data.cep,
      numero: data.numero,
      complemento: data.complemento,
      logradouro: data.logradouro,
      bairro: data.bairro,
      localidade: data.localidade,
      uf: data.uf,
      estado: data.estado,
      regiao: data.regiao,
    };
    // Verifica se telefones não estão vazios e separa os telefones de forma correta
    const telefones =
      data.telefones && data.telefones.length > 0 ? data.telefones : [];

    // Estrutura final que será enviada para a API
    const requestData = {
      dados_candidato: dadosCandidato,
      enderecos: enderecos,
      telefones: telefones,
    };

    try {
      const response = await makeApiCall(
        "candidato-detalhes/", // Endpoint da API
        requestData,
        "POST" // Método HTTP
      );
      setApiResponse(JSON.stringify(response, null, 2)); // Armazena a resposta para exibição
      setErrorRequest(false);
      navigate("/login", {
        state: { message: "Dados cadastrados com sucesso!" },
      });
    } catch (error) {
      console.error("Erro ao salvar:", error.message);
      setApiResponse(error.response?.data || error.message);
      setErrorRequest(true);
    }
  };

  const [linkedin, setLinkedin] = useState("");
  const [github, setGithub] = useState("");
  const [cep, setCep] = useState("");
  const [numero, setNumero] = useState("");
  const [complemento, setComplemento] = useState("");

  // Verifica se está autenticado -> redireciona para Login ou popula o formulário
  useEffect(() => {
    if (!hasFetched.current) {
      hasFetched.current = true;

      const fetchCandidatoDetalhes = async () => {
        if (!isLoggedIn()) {
          navigate("/login");
          return;
        }

        try {
          const response = await makeApiCall("candidato-detalhes/", {}, "GET");

          const userData = getResetData(response);

          reset(userData);
          setEndereco(userData.endereco);
          setIsDeficiente(userData.deficiencia);

          // Atualiza o valor inicial de linkedin no formulário
          setLinkedin(userData.linkedin || ""); // Atualiza o estado local
          setValue("linkedin", userData.linkedin || ""); // Atualiza o formulário
          setGithub(userData.github || ""); // Atualiza o estado local
          setValue("github", userData.github || ""); // Atualiza o formulário
          setCep(userData.cep || ""); // Atualiza o estado local
          setValue("cep", userData.cep || ""); // Atualiza o formulário
          setNumero(userData.numero || ""); // Atualiza o estado local
          setValue("numero", userData.numero || ""); // Atualiza o formulário
          setComplemento(userData.complemento || ""); // Atualiza o estado local
          setValue("complemento", userData.complemento || ""); // Atualiza o formulário
        } catch (error) {
          console.error("Erro ao buscar detalhes do candidato:", error.message);
        }
      };

      fetchCandidatoDetalhes();
    }
  }, [navigate, setValue, reset, linkedin, github]);

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" component="h1" gutterBottom>
        Dados do Candidato
      </Typography>

      {/* Exibe alertas de erro, caso existam */}
      {errorRequest && (
        <Alert severity="error">
          {Array.isArray(apiResponse)
            ? apiResponse.map((message, index) => (
                <Typography key={index}>{message}</Typography>
              ))
            : apiResponse}
        </Alert>
      )}

      {/* Formulário */}
      <form onSubmit={handleSubmit(onSubmit)}>
        {/* Campo de seleção: Gênero */}
        <FormControl fullWidth margin="normal">
          <InputLabel>Gênero</InputLabel>
          <Select
            {...register("genero", { required: "O gênero é obrigatório" })}
            error={!!errors.genero}
            value={genero}
            onChange={(e) => setValue("genero", e.target.value)}
          >
            <MenuItem value="masculino">Masculino</MenuItem>
            <MenuItem value="feminino">Feminino</MenuItem>
            <MenuItem value="nao_respondido">Prefiro não responder</MenuItem>
          </Select>
          {errors.genero && (
            <Typography color="error">{errors.genero.message}</Typography>
          )}
        </FormControl>

        {/* Checkbox para deficiência */}
        <FormControlLabel
          control={
            <Checkbox
              {...register("deficiente")}
              checked={isDeficiente}
              onChange={handleDeficienteChange}
            />
          }
          label="Possui deficiência?"
        />

        {/* Campo de tipo de deficiência (exibido apenas se checkbox for marcado) */}
        {isDeficiente && (
          <TextField
            label="Tipo de deficiência"
            variant="outlined"
            fullWidth
            margin="normal"
            {...register("tipo_deficiencia")}
            error={!!errors.tipo_deficiencia}
            helperText={errors.tipo_deficiencia?.message}
          />
        )}

        {/* LinkedIn e GitHub */}
        <TextField
          label="LinkedIn"
          variant="outlined"
          fullWidth
          margin="normal"
          {...register("linkedin")}
          value={linkedin || ""}
          onChange={(e) => setValue("linkedin", e.target.value)}
          error={!!errors.linkedin}
          helperText={errors.linkedin?.message}
        />
        <TextField
          label="GitHub"
          variant="outlined"
          fullWidth
          margin="normal"
          {...register("github")}
          value={github || ""}
          onChange={(e) => setValue("github", e.target.value)}
          error={!!errors.github}
          helperText={errors.github?.message}
        />

        {/* Endereço */}
        <Typography variant="h6">Endereço</Typography>
        <TextField
          label="CEP"
          variant="outlined"
          fullWidth
          margin="normal"
          inputRef={cepRef}
          {...register("cep", { required: "O CEP é obrigatório" })}
          value={cep || ""}
          onChange={(e) => setCep("cep", e.target.value)}
          onBlur={(e) => buscarEndereco(e.target.value)}
          error={!!errors.cep}
          helperText={errors.cep?.message}
        />

        {/* Renderiza os campos do endereço automaticamente preenchidos */}
        {["logradouro", "bairro", "localidade", "uf", "estado", "regiao"].map(
          (field) => (
            <TextField
              key={field}
              label={field.charAt(0).toUpperCase() + field.slice(1)}
              variant="outlined"
              fullWidth
              margin="normal"
              value={endereco[field] || ""}
              disabled
            />
          )
        )}

        {/* Campos adicionais do endereço */}
        <TextField
          label="Número"
          variant="outlined"
          fullWidth
          margin="normal"
          {...register("numero", { required: "O número é obrigatório" })}
          value={numero || ""}
          onChange={(e) => setValue("numero", e.target.value)}
          error={!!errors.numero}
          helperText={errors.numero?.message}
        />
        <TextField
          label="Complemento"
          variant="outlined"
          fullWidth
          margin="normal"
          {...register("complemento")}
          value={complemento || ""}
          onChange={(e) => setValue("complemento", e.target.value)}
          error={!!errors.complemento}
          helperText={errors.complemento?.message}
        />

        {/* Seção de Telefones */}

        <Box sx={{ mt: 3, mb: 2 }}>
          <Box
            display="flex"
            alignItems="center"
            justifyContent="space-between"
            mb={2}
          >
            <Typography variant="h6">Telefones</Typography>
            <Tooltip
              title={
                fields.length >= 3
                  ? "Máximo de 3 telefones atingido"
                  : "Adicionar telefone"
              }
            >
              <span>
                <IconButton
                  color="primary"
                  onClick={handleAddPhone}
                  disabled={fields.length >= 3}
                >
                  <AddIcon />
                </IconButton>
              </span>
            </Tooltip>
          </Box>

          {fields.map((field, index) => (
            <Telefone
              key={field.id}
              index={index}
              field={field}
              watch={watch}
              register={register}
              setValue={setValue}
              remove={handleRemovePhone}
              error={errors?.telefones?.[index]}
            />
          ))}
        </Box>

        {/* Botão de envio do formulário */}
        <Button type="submit" variant="contained" color="primary" fullWidth>
          Enviar
        </Button>
      </form>
    </Container>
  );
};

export default CandidatoDetalhes;
