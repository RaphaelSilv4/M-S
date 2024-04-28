import React from 'react';
import { Link } from 'react-router-dom';
import Input from '../Input/input';
import { BiSearchAlt2 } from 'react-icons/bi';

import styles from './Header.module.css';

const Header = () => {
    return (
        <header className={styles.header}>
            <div className={styles.logo}>M & S</div>
            <Input type="text" className={styles.search_bar} placeholder="Pesquisar..."/>
            <Link to="/" className={styles.login}>Login</Link>
        </header>
    );
};

export default Header;
