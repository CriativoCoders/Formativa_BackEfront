import estilo from './ListaProfessores.module.css';
import { useState } from 'react';


export function ListaProfessores() {
  const [professores, setProfessores] = useState([]);
  const [idAtual, setIdAtual] = useState(1);

  const [novoProfessor, setNovoProfessor] = useState({
    nome: '',
    disciplina: '',
  });
  
  
  const adicionarProfessor = (e) => {
    e.preventDefault();
    const professor = {
      id: idAtual,
      nome: novoProfessor.nome,
      disciplina: novoProfessor.disciplina,
    };
    setProfessores([...professores, professor]);
    setNovoProfessor({
      nome: '',
      disciplina: '',
    });
    setIdAtual(idAtual + 1);
  };


  const handleInputChange = (e) => {
    setNovoProfessor({
      ...novoProfessor,
      [e.target.name]: e.target.value,
    });
  };


  const deletarProfessor = (id) => {
    setProfessores(professores.filter((professor) => professor.id !== id));
  };

  return (
    <div className={estilo.principal}>
      <h1>Lista de Professores</h1>
      <form onSubmit={adicionarProfessor} className={estilo.formulario}>
        <label>Nome:</label>
        <input
          type="text"
          name="nome"
          value={novoProfessor.nome}
          onChange={handleInputChange}
        />
        <label>Disciplina:</label>
        <input
          type="text"
          name="disciplina"
          value={novoProfessor.disciplina}
          onChange={handleInputChange}
        />
        <button type="submit">Adicionar Professor</button>
      </form>
      <table className={estilo.tabela}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Disciplina</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {professores.map((professor) => (
            <tr key={professor.id}>
              <td>{professor.id}</td>
              <td>{professor.nome}</td>
              <td>{professor.disciplina}</td>
              <td>
                <button onClick={() => deletarProfessor(professor.id)}>
                  Deletar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}