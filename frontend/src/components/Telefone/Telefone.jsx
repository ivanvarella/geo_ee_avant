import {
  Box,
  Select,
  MenuItem,
  TextField,
  FormControl,
  InputLabel,
  IconButton,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import IMask from "imask";
import { useEffect, useRef } from "react";
import PropTypes from "prop-types";

const Telefone = ({ index, watch, register, setValue, remove, error }) => {
  const phoneRef = useRef(null);

  // Aplicar máscara ao telefone
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

  // Aplicar máscara sempre que o tipo mudar
  useEffect(() => {
    const tipo = watch(`telefones.${index}.tipo`);
    if (phoneRef.current) {
      applyPhoneMask(phoneRef.current, tipo);
    }
  }, [watch, index]);

  return (
    <Box
      sx={{
        display: "flex",
        gap: 2,
        mb: 2,
        alignItems: "center",
      }}
    >
      {/* Campo de seleção: Tipo */}
      <FormControl sx={{ minWidth: 150 }}>
        <InputLabel>Tipo</InputLabel>
        <Select
          {...register(`telefones.${index}.tipo`, {
            required: "O tipo do telefone é obrigatório",
          })}
          defaultValue="celular"
          onChange={(e) => {
            setValue(`telefones.${index}.tipo`, e.target.value);
          }}
          error={!!error?.tipo}
        >
          <MenuItem value="residencial">Residencial</MenuItem>
          <MenuItem value="comercial">Comercial</MenuItem>
          <MenuItem value="celular">Celular</MenuItem>
        </Select>
      </FormControl>

      {/* Campo de entrada: Número */}
      <TextField
        inputRef={phoneRef}
        {...register(`telefones.${index}.numero`, {
          required: "O número do telefone é obrigatório",
        })}
        label="Número"
        variant="outlined"
        error={!!error?.numero}
        helperText={error?.numero?.message}
        fullWidth
      />

      {/* Botão para remover telefone */}
      <IconButton color="error" onClick={() => remove(index)}>
        <DeleteIcon />
      </IconButton>
    </Box>
  );
};

// Declaração dos PropTypes fora do componente
Telefone.propTypes = {
  index: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
  field: PropTypes.object, // Ajuste conforme o tipo esperado
  watch: PropTypes.func.isRequired, // Se for opcional, remova o `isRequired`
  register: PropTypes.func.isRequired,
  setValue: PropTypes.func.isRequired,
  remove: PropTypes.func.isRequired,
  error: PropTypes.shape({
    tipo: PropTypes.string,
    numero: PropTypes.shape({
      message: PropTypes.string,
    }),
  }),
};

export default Telefone;
