export function getResetData(data) {
  const candidatoData = data.dados_candidato[0];
  const enderecoData = data.endereco[0];
  const telefonesData = data.telefones;

  return {
    genero: candidatoData.genero || "",
    tipo_deficiencia: candidatoData.tipo_deficiencia || "",
    linkedin: candidatoData.linkedin || "",
    github: candidatoData.github || "",
    cep: enderecoData?.cep || "",
    numero: enderecoData?.numero || "",
    complemento: enderecoData?.complemento || "",
    endereco: {
      logradouro: enderecoData?.logradouro || "",
      bairro: enderecoData?.bairro || "",
      localidade: enderecoData?.localidade || "",
      uf: enderecoData?.uf || "",
      estado: enderecoData?.estado || "",
      regiao: enderecoData?.regiao || "",
    },
    telefones: telefonesData || [],
    deficiencia: !!candidatoData.deficiencia,
  };
}
