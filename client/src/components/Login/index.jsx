import { useState } from 'react';
import api from '../../axios';

import styles from './login.module.css';

function Login() {
    const [email, setEmail] = useState('');
    const [senha, setSenha] = useState('');

    async function onSubmitHandler(event) {
        event.preventDefault();

        try {
            const response = await api.post('/login/', {
                email,
                senha
            });

            if (response.status === 200) {
                // Login bem-sucedido
                window.location.href = '/home'; // Redireciona para a página home
            } else {
                // Exibir mensagem de erro de login
                console.error('Erro ao fazer login');
            }
        } catch (error) {
            // Exibir mensagem de erro
            console.error('Erro ao fazer login:', error);
        }
    }


    return (
        <div className={styles.mainContainer}>
            <div className={styles.container}>
                <div className={styles.containerMenssagem}>
                    <div className={styles.textSigla}>
                        <span className="sigla">M & S</span>
                    </div>
                    <div className={styles.textMenssagem}>
                        <span className="menssagem">Bem-vindo de volta!</span>
                    </div>
                    <div className={styles.subMenssagem}>
                        <span className="menssagem-login">Faça seu login ao lado.</span>
                    </div>
                </div>
                <div className={styles.containerLogin}>
                    <form className={styles.loginForm} onSubmit={onSubmitHandler}>
                        <h1 className={styles.loginMenssage}>Faça seu Login</h1>
                        <div className={styles.textfild}>
                            <input type="email"
                                name='email'
                                placeholder='Email'
                                value={email}
                                onChange={(e) => setEmail(e.target.value)} />
                        </div>
                        <div className={styles.textfild}>
                            <input type="password"
                                name='senha'
                                placeholder='Senha'
                                value={senha}
                                onChange={(e) => setSenha(e.target.value)} />
                        </div>
                        <div className={styles.containerLoginFormBtn}>
                            <button to='/home' className={styles.loginBtn} type='submit'>ENTRAR</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default Login;

