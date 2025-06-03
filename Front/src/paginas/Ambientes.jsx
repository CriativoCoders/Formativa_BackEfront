import { BarraNavegacao } from '../Componentes/BarraNavegacao';
import { Cabecalho } from '../Componentes/Cabecalho';
import { Menu } from '../Componentes/Menu';
import { Rodape } from '../Componentes/Rodape';
import './Inicial.css'; // Arquivo com o CSS de layout

export function Inicial() {
  return (
    <div className="pagina">
      <BarraNavegacao/>
      <Cabecalho/>
      <Menu/>
      <Rodape/>
    </div>
  );
}
