import { useState, useEffect } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faCheck, faX } from '@fortawesome/free-solid-svg-icons'
import Input from './input'


library.add(faCheck, faX)


export default function ModalNewPlate(props) {
    const [getToken, setToken] = useState(sessionStorage.getItem('token'));

    // Is valid?
    const [validNumber, setValidNumber] = useState(false)
    const [validCity, setValidCity] = useState(false)
    const [validManufac, setValidManufac] = useState(false)
    const [validModel, setValidModel] = useState(false)
    const [validColor, setValidColor] = useState(false)
    const [validYear, setValidYear] = useState(false)

    function close_modal() {
        let modal = document.getElementById("ModalNew");
        modal.style.display = 'none'
    }

    // Validate
    function validate_number(event) {
        const value = event.target.value
        if ( value.length == 7) {
            props.setNumber(value)
            setValidNumber(true)
        } else {
            props.setNumber(value)
            setValidNumber(false)
        }
    }

    function validate_city(event) {
        const value = event.target.value
        if (value.includes("-") && value.length > 4) {
            props.setCity(value)
            setValidCity(true)
        } else {
            props.setCity(value)
            setValidCity(false)
        }
    }

    function validate_manufac(event) {
        const value = event.target.value
        if (value.length >= 2) {
            props.setManufac(value)
            setValidManufac(true)
        } else {
            props.setManufac(value)
            setValidManufac(false)
        }
    }

    function validate_model(event) {
        const value = event.target.value
        if (value.length >= 2) {
            props.setModel(value)
            setValidModel(true)
        } else {
            props.setModel(value)
            setValidModel(false)
        }
    }

    function validate_color(event) {
        const value = event.target.value
        if (value.length >= 4) {
            props.setColor(value)
            setValidColor(true)
        } else {
            props.setColor(value)
            setValidColor(false)
        }
    }

    function validate_year(event) {
        const value = event.target.value
        if ( 2000 < value && value < 2024) {
            props.setYear(value)
            setValidYear(true)
        } else {
            setValidYear(false)
            props.setYear(value)
        }
    }

    function validate_qru(event) {
        const value = event.target.value
        props.setQru(value)
    }


    function check_plate_validate() {
        if (validNumber && validCity && validManufac && validModel && validColor && validYear) {
            if (props.type) {
                props.create()
            } else {
                props.edit()
            }
            close_modal()
        } else {
            const tip = document.getElementById("modalTip")
            tip.innerText = "Prencha os dados corretamente"
        }
    }


    function delete_plate() {
        let url = `http://127.0.0.1:8000/plates/del=${props.id}/`
        let data = {method: 'DELETE', 
                    headers: {Authorization: 'Token '+ getToken},
                    }
        fetch(url, data)
        .then(() =>{ 
            props.update()
            close_modal()
        })
    }

    useEffect(() => {
        const fakeNumber = { target: { value: props.number || ''} };
        validate_number(fakeNumber)
        const fakeCity = { target: { value: props.city || '-RS'} };
        validate_city(fakeCity)
        const fakeManufac = { target: { value: props.manufac || ''} };
        validate_manufac(fakeManufac)
        const fakeModel = { target: { value: props.model || ''} };
        validate_model(fakeModel)
        const fakeColor = { target: { value: props.color || ''} };
        validate_color(fakeColor)
        const fakeYear = { target: { value: props.year || 2001} };
        validate_year(fakeYear)
        const tip = document.getElementById("modalTip")
        tip.innerText = ""
    }, [props.number])


    return (
        <div className="modal-background" id="ModalNew" onClick={close_modal}>
            <div className="div-modal" onClick={e => e.stopPropagation()}>
                <div className="align-inputs">
                    <Input  validate={validate_number} valid={validNumber} value={props.number} placeholder='Digite a placa' ></Input>
                    <Input  validate={validate_city} valid={validCity} value={props.city} placeholder='Digite cidade'></Input>
                    <Input  validate={validate_manufac} valid={validManufac} value={props.manufac} placeholder='Digite o fabricante'></Input>
                    <Input  validate={validate_model} valid={validModel} value={props.model} placeholder='Digite o modelo'></Input>
                    <Input  validate={validate_color} valid={validColor} value={props.color} placeholder='Digite a cor'></Input>
                    <Input  type={'number'} validate={validate_year} valid={validYear} value={props.year} placeholder='Digite o ano'></Input>
                    <Input  validate={validate_qru} valid={true} value={props.qru} placeholder='Digite a qru'></Input><br/>
                </div>
                <div className='align-btns'>
                    <button className='btn' onClick={check_plate_validate}> Salvar </button>
                    <button className='btn' onClick={delete_plate} style={{display: props.save? 'block' : 'none' }}> Deletar </button>
                </div>
                <a className='login-tip' id='modalTip'> </a>
            </div>
        </div>
    )
}