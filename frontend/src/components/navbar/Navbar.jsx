import React from 'react'
import './navbar.css';

const Navbar = () => {


    return (
        <div className="header">
          <div className="logo">
            <button>Icops</button>
          </div>
          <div className="buttons">
            <button className="button">S'inscrire</button>
            <button className="button">Connexion</button>
          </div>
        </div>
      );
    }

export default Navbar