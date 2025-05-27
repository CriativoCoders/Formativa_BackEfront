import { BarraNavegacao } from '../Componentes/BarraNavegacao';
import { Cabecalho } from '../Componentes/Cabecalho';
import { ListaProfessores } from '../Componentes/ListaProfessores';
import { Rodape } from '../Componentes/Rodape';

export function Professores() {
  return (
    <div className="pagina">
      <BarraNavegacao />
      <Cabecalho/>
      <ListaProfessores/>
      <Rodape/>
    </div>
  );
}
