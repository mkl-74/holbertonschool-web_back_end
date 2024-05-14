// Fonction getBudgetForCurrentYear
function getBudgetForCurrentYear(income, gdp, capita) {
  const currentYear = 2021;

  return {
    [`income-${currentYear}`]: income,
    [`gdp-${currentYear}`]: gdp,
    [`capita-${currentYear}`]: capita,
  };
}

// Exportation de la fonction getBudgetForCurrentYear par défaut
export default getBudgetForCurrentYear;
