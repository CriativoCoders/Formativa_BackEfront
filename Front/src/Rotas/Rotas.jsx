import { Route, Routes } from 'react-router-dom';
import { Inicial } from '../Paginas/Inicial'; // renomeei para Inicial com letra maiúscula
import { Login } from '../paginas/Login';
import { Menu } from '../paginas/Menu'; // importe o componente Menu

export function Rotas(){
    return(
        <Routes>
            <Route path='/' element={<Login/>}/>

            <Route path='/inicial' element={<Inicial/>}>
                <Route index element={<Menu/>}/>
            </Route>
        </Routes>
    )
}