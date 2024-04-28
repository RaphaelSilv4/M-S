import { Link, useNavigate} from 'react-router-dom';
import { useState } from 'react';
import api from '../../axios';

import styles from './register.module.css';

function Register() {

  const [email, setEmail] = useState('')
  const [name, setName] = useState('')
  const [password, setPassword] = useState('')
  const navegate = useNavigate();

  async function onSubmitHandler(event) {
    event.preventDefault();
    try {
      const response = await api.post('/routes/cliente', {
        nome: name,
        email: email,
        senha: password
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      console.log(response);

      // Redireciona para a página home após o cadastro bem-sucedido
      navegate('/');
    } catch (error) {
      console.log(error);
    }
  }



  return (
    <div className={styles.mainContainer}>
      <div className={styles.containerLoginCadastro}>
        <div className={styles.containerLogin}>
          <div className={styles.textSigla}>
            <span className="sigla">M & S</span>
          </div>
          <div className={styles.textMenssagem}>
            <span className="menssagem">Bem-vindo de volta!</span>
          </div>
          <div className={styles.textMenssagem2}>
            <span className="menssagem-login">Faça seu login abaixo.</span>
          </div>
          <div className={styles.containerLoginFormBtn}>
            <Link to='/' className={styles.linkloginBtn}>ENTRAR</Link>
          </div>
        </div>
        <div className={styles.containerCadastro}>
          <div className={styles.cadastro}>
            <form className={styles.cadastroForm} onSubmit={onSubmitHandler}>
              <h1 className={styles.criarConta}>Criar Conta</h1>
              <h1 className={styles.subMenssagem}>Cadastre-se com seu email</h1>
              <div className={styles.textfild}>
                <input
                  type="email"
                  name='email'
                  placeholder='Email'
                  onChange={(e) => setEmail(e.target.value)}
                />
              </div>
              <div className={styles.textfild}>
                <input
                  type="text"
                  name='name'
                  placeholder='Nome'
                  onChange={(e) => setName(e.target.value)}
                />
              </div>
              <div className={styles.textfild}>
                <input
                  type="password"
                  name='password'
                  placeholder='Senha'
                  onChange={(e) => setPassword(e.target.value)}
                />
              </div>
              <div className={styles.containerCadastroFormBtn}>
                <button className={styles.linkButton} type='submit'>CADASTRAR</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Register;
