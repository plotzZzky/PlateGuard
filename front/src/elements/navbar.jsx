import { useState } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUser, faBars, faCar, faHome } from '@fortawesome/free-solid-svg-icons'
library.add(faUser, faBars, faCar, faHome)

import './navbar.css'


export default function NavBar() {
  const [getToken, setToken] = useState(sessionStorage.getItem('token'));

  function OpenMenu() {
    let navbar = document.getElementsByClassName("menu")[0];
    if (navbar.className == "menu") {
      navbar.classList.add("responsive")
    } else {
      navbar.className = "menu"
    }
  }

  function go_app() {
    if (getToken == undefined) {
      location.href = "/plateguard/login/"
    } else {
      location.href = "/plateguard/app/"
    }
  }

  return (
    <div className="navbar">

      <div className='navbar-align'>

        <div className="menu" id="menu">
          <a className="menu-icon" onClick={OpenMenu}>
            <FontAwesomeIcon icon="fa-solid fa-bars fa-2xl" />
          </a>

          <div className="menu-item" onClick={() => location.href = "/plateguard/"}>
            <a><FontAwesomeIcon icon="fa-solid fa-home" className='icon-menu' /> Inicio </a>
          </div>

          <div className="menu-item" onClick={go_app}>
            <a><FontAwesomeIcon icon="fa-solid fa-car" className='icon-menu' /> App </a>
          </div>

          <div className="menu-item" onClick={() => location.href = "/plateguard/login/"}>
            <a><FontAwesomeIcon icon="fa-solid fa-user" className='icon-menu' /> Entrar </a>
          </div>

        </div>
      </div>
    </div>
  )
}