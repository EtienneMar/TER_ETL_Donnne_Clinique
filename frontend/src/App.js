import React from 'react'
import './App.css'
import { Navbar, Hometitle, DragAndDrop } from './components'

const App = () => {
  return (
    <div className='App'>
      <Navbar />
      <Hometitle />
      <DragAndDrop /> 
    </div>
  )
}

export default App

/*Ceci est le fichier principale qui sert d'appel aux différent composant react 
Navbar va appeler le code contenu dans navbar ect.. ect..
Pour pouvoir importer un nouveau composant il faut l'important dans la ligne 


import { Navbar, Hometitle, DragAndDrop } from './components'

*/ 