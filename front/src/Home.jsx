import { useState } from 'react';
import NavBar from './elements/navbar'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faGithub } from '@fortawesome/free-brands-svg-icons'

library.add(faGithub )


export default function Home() {
    const [getToken, setToken] = useState(sessionStorage.getItem('token'));
    const faq = [
        {
            'question': 'O que é essa plataforma?',
            'answer': 'A nossa plataforma é um site para salvar informações de carros para empresas de segurança de portarias e estacionamentos.'
        },
        {
            'question': 'Como ela funciona?',
            'answer': 'As informações são armazenadas de forma segura, permitindo que as empresas possam acessá-las facilmente quando necessário para garantir a segurança de suas propriedades.'
        },
        {
            'question': 'Quais as vantagens de usar a plataforma?',
            'answer': 'Há diversas vantagens em usar a plataforma, como: facilidade de acesso às informações dos veículos cadastrados, maior eficiência na segurança das propriedades monitoradas e armazenamento seguro de informações de veículos.'
        },
        {
            'question': 'É possível acessar as informações dos veículos cadastrados a partir de qualquer lugar?',
            'answer': 'Sim, a plataforma é acessível a partir de qualquer dispositivo com acesso à internet.'
        },
        {
            'question': 'Como faço para começar a usar a plataforma?',
            'answer': 'Para começar a usar a plataforma, basta se cadastrar e criar um posto de serviço ou acessar um ja existente'
        }
    ]

    const site_desc = `Nosso site é a solução ideal para empresas de segurança de portarias e estacionamentos que buscam mais eficiência e segurança no controle de entrada e saída de veículos. 
    Com nossa plataforma, é possível armazenar informações de carros de forma segura e acessível, garantindo maior controle sobre as atividades nas propriedades monitoradas. 
    Além disso, oferecemos vantagens como possibilidade de acompanhar a movimentação de veículos em tempo real, facilidade na geração de relatórios e análises sobre a movimentação de veículos nas propriedades, e redução de custos com sistemas de segurança e monitoramento de propriedades.`

    function to_login() {
        location.href = "/plates/login/"
    }

    function to_notes() {
        if (getToken == undefined) {
            location.href = "/plateguard/login/"
        } else {
            location.href = "/plateguard/notes/"
        }
    }

    return (
        <>
            <NavBar></NavBar>

            <div className='page-home'>
                <h1> Bem vindo ao PlateGuard</h1>
                <h3>  O melhor amigo do seu estacionamento </h3> 
                <p className='home-text'> PlateGuard é uma plataforma para salvar informações de carros para empresas de segurança de portarias e estacionamentos. 
                As informações são armazenadas de forma segura, permitindo acessá-las facilmente para garantir a segurança de suas propriedades.</p> 
            </div>

            <div className='page-home'>
                <h2> Sobre: </h2>
                <p className='home-text'> {site_desc} </p>
            </div>

            <div className='page-home'>
                <h2> Duvidas frequentes: </h2>
                {faq.map((data) => (
                    <details className='home-details'> 
                        <summary className='home-summary'>
                            {data.question} 
                        </summary>
                        <p className='home-answer'> {data.answer} </p>
                    </details>
                ))}
            </div>

            <footer>
                <a href='https://www.github.com/plotzzzky'> Dev: Plotzky <FontAwesomeIcon icon="fa-brands fa-github" /></a>
            </footer>
        </>
  )
}
