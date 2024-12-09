import { useState, useEffect, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { makeApiCall } from "../../services/api";
import { values } from "lodash";
import {
  Container,
  TextField,
  Button,
  Typography,
  Alert,
  Box,
} from "@mui/material";
// useFieldArray -> Array de campos telefone
import { useFieldArray, useForm } from "react-hook-form";
import PropTypes from "prop-types";
import IMask from "imask"; // Importando o IMask

const CadastroUser = ({ tipo = "candidato" }) => {
  const [apiResponse, setApiResponse] = useState("");
  const [errorRequest, setErrorRequest] = useState(false);
  const navigate = useNavigate();

  // Utilizando o react-hook-form
  const {
    register,
    handleSubmit,
    formState: { errors },
    watch,
    control, // Para o array de telefones
  } = useForm();

  // Hook-form: Gerenciar um array de campos telefone
  const { fields, append, remove } = useFieldArray({
    control, // control props comes from useForm (optional: if you are using FormProvider)
    name: "telefone", // unique name for your Field Array
  });

  // Referência do campo CPF
  const cpfRef = useRef(null);

  // Função para aplicar a máscara do CPF utilizando IMask
  useEffect(() => {
    if (cpfRef.current) {
      IMask(cpfRef.current, {
        mask: "000.000.000-00",
      });
    }
  }, []);

  const onSubmit = async (data) => {
    // Adiciona o tipo aos dados do formulário antes de enviar
    data.tipo = tipo; // O tipo pode ser "candidato" ou "responsavel"
    makeApiCallCadastroUser("candidato/", data);
  };

  // Função para fazer a chamada à API utilizando makeApiCall de api.js
  const makeApiCallCadastroUser = async (endpoint, data) => {
    try {
      const response = await makeApiCall(endpoint, data, "POST"); // Chama a função makeApiCall de api.js
      setApiResponse(JSON.stringify(response, null, 2));
      setErrorRequest(false);
    } catch (error) {
      console.log("Error:", error);
      setApiResponse(error.response.data);
      console.error("Erro ao fazer a chamada à API:", error);
      if (error.response) {
        setErrorRequest(true);
      }
    }
  };

  const errorMessages = values(apiResponse).map((message) => message[0]);

  // Monitorando o campo de senha para validar a confirmação
  const password = watch("password");

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" component="h1" gutterBottom>
        Cadastro de {tipo === "candidato" ? "Candidato" : "Responsável"}
      </Typography>
      {errorRequest && (
        <Alert severity="error">
          {errorMessages.map((message, index) => (
            <Typography key={index}>{message}</Typography>
          ))}
        </Alert>
      )}
      <form onSubmit={handleSubmit(onSubmit)}>
        <TextField
          label="Nome"
          variant="outlined"
          fullWidth
          margin="normal"
          {...register("first_name", { required: "O nome é obrigatório" })}
          error={!!errors.first_name}
          helperText={errors.first_name?.message}
        />
        <TextField
          label="Sobrenome"
          variant="outlined"
          fullWidth
          margin="normal"
          {...register("last_name", { required: "O sobrenome é obrigatório" })}
          error={!!errors.last_name}
          helperText={errors.last_name?.message}
        />
        <TextField
          label="E-mail"
          variant="outlined"
          fullWidth
          margin="normal"
          type="email"
          {...register("email", { required: "O e-mail é obrigatório" })}
          error={!!errors.email}
          helperText={errors.email?.message}
        />
        <TextField
          label="Senha"
          variant="outlined"
          fullWidth
          margin="normal"
          type="password"
          {...register("password", { required: "A senha é obrigatória" })}
          error={!!errors.password}
          helperText={errors.password?.message}
        />
        <TextField
          label="Confirmar Senha"
          variant="outlined"
          fullWidth
          margin="normal"
          type="password"
          {...register("confirm_password", {
            required: "A confirmação de senha é obrigatória",
            validate: (value) =>
              value === password || "As senhas não coincidem", // Usando a variável password aqui
          })}
          error={!!errors.confirm_password}
          helperText={errors.confirm_password?.message}
        />

        <TextField
          label="CPF"
          variant="outlined"
          fullWidth
          margin="normal"
          inputRef={cpfRef} // Referência do campo CPF
          {...register("cpf", {
            required: "O CPF é obrigatório",
            pattern: {
              value: /^\d{3}\.\d{3}\.\d{3}-\d{2}$/,
              message: "O CPF deve estar no formato 000.000.000-00",
            },
          })}
          error={!!errors.cpf}
          helperText={errors.cpf?.message}
        />
        <TextField
          label="Data de Nascimento"
          type="date"
          fullWidth
          margin="normal"
          {...register("data_nascimento", {
            required: "A data de nascimento é obrigatória",
          })}
          error={!!errors.data_nascimento}
          helperText={errors.data_nascimento?.message}
          InputLabelProps={{
            shrink: true,
          }}
        />
        {/* Para criação do array de campos telefone */}
        {fields.map((field, index) => (
          <>
            <TextField
              label="Telefone"
              variant="outlined"
              type="tel"
              key={field.id}
              {...register(`telefoneCandidato.${index}.value`)}
            />
            <Button onClick={() => remove(index)}>Remover Telefone</Button>
          </>
        ))}
        <Button onClick={() => append({ value: "" })}>
          Adicionar Telefone
        </Button>
        {/* Array de campos telefone */}

        <Box mt={2}>
          <Button variant="contained" color="primary" type="submit" fullWidth>
            Registrar
          </Button>
        </Box>
      </form>
      <Box mt={2}>
        <Button
          variant="outlined"
          color="primary"
          onClick={() => navigate("/")}
          fullWidth
        >
          Voltar
        </Button>
      </Box>
    </Container>
  );
};

// Validação da prop 'tipo'
CadastroUser.propTypes = {
  tipo: PropTypes.string,
};

export default CadastroUser;
