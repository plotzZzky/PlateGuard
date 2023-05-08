import { useState, useEffect } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faFileCirclePlus } from '@fortawesome/free-solid-svg-icons'
import ModalNewPlate from '../elements/modalNew'
import PlateCard from '../elements/plateCards'

library.add(faFileCirclePlus)


export default function App() {
    const [getToken, setToken] = useState(sessionStorage.getItem('token'));
    const [modalNew, setModalNew] = useState(false);
    const [getSave, setSave] = useState(true);

    //Plates
    const [getCards, setCards] = useState([]);

    // Inputs
    const [getNumber, setNumber] = useState("");
    const [getCity, setCity] = useState("");
    const [getModel, setModel] = useState("");
    const [getManufac, setManufac] = useState("");
    const [getColor, setColor] = useState("");
    const [getYear, setYear] = useState();
    const [getQru, setQru] = useState("");
    const [getId, setId] = useState();

    function check_login() {
        if (getToken == undefined) {
            location.href = "/plateguard/login/";
        } else {
            get_plates()
        }
    }

    // Get list with all plates
    function get_plates() {
        let url = "http://127.0.0.1:8000/plates/"
        let data = {method: 'GET', 
                    headers: {Authorization: 'Token '+ getToken}}
        fetch(url, data)
        .then((res) => res.json())
        .then((data) =>{ 
            create_list(data['plates'])
        })
    }

    function create_list(value) {
        setCards(
            value.map((data) => (
                <PlateCard data={data} show={() => set_modal(data, true)}></PlateCard>
        )))
    }

    function set_modal(data, type) {
        setNumber(data.number || '')
        setCity(data.city || '-RS')
        setManufac(data.manufac || '')
        setModel(data.model || '')
        setColor(data.color || '')
        setYear(data.year || 2001)
        setQru(data.qru || 43)
        setId(data.id || '')
        show_modal(type)
    }

    function show_modal(type) {
        const modal = document.getElementById("ModalNew");
        let display = window.getComputedStyle(modal).getPropertyValue("display");
        if (display == "none") {
          modal.style.display = "block";
        } else {
          modal.style.display = "none";
        }
        setSave(type);
    }

    // create form for new plate or edit plate
    function create_form() {
        const formData = new FormData();
        formData.append("number", getNumber);
        formData.append("city", getCity);
        formData.append("manufac", getManufac);
        formData.append("model", getModel);
        formData.append("color", getColor);
        formData.append("year", getYear);
        formData.append("qru", getQru);

        return formData
    }

    function create_new_plate() {
        let url = "http://127.0.0.1:8000/plates/add/"
        const formData = create_form()
        let data = {method: 'POST', 
                    headers: {Authorization: 'Token '+ getToken},
                    body: formData
                }
        fetch(url, data)
        .then(() =>{ 
            get_plates()
        })
    }

    function edit_plate() {
        let url = `http://127.0.0.1:8000/plates/edit=${getId}/`
        const formData = create_form()
        let data = {method: 'POST', 
                    headers: {Authorization: 'Token '+ getToken},
                    body: formData
                }
        fetch(url, data)
        .then(() =>{ 
            get_plates()
        })
    }

    function filter_plate() {
        let value = document.getElementById("FilterInput").value.toLowerCase()
        let item = document.getElementsByClassName("plate-card")
            for (let x = 0; x < item.length; x++) {
            let number = item[x].children[0].children[0].innerHTML.toLowerCase()
            let city = item[x].children[0].children[1].innerHTML.toLowerCase()
            if ( number.indexOf(value) > -1 || city.indexOf(value) > -1) {
                item[x].style.display = "flex";
            } else {
                item[x].style.display = "none";
            }
        }
    }

    useEffect(() => {
        check_login()
    }, [])


    return(
        <>
            <nav className='app-navbar'>
                <input placeholder='Buscar' className='find-plate' id='FilterInput' onChange={filter_plate}></input>
                <FontAwesomeIcon icon="fa-solid fa-file-circle-plus" className='new-plate-icon' onClick={() => set_modal({}, false)}/>
            </nav>
            <div className='page' style={{paddingTop: '2em'}}>
                <div className='align-cards'>
                    {getCards}
                </div>
            </div>
            <ModalNewPlate modal={setModalNew} save={getSave} create={create_new_plate} update={get_plates} edit={edit_plate}

                number={getNumber} city={getCity} model={getModel} manufac={getManufac} 
                year={getYear} color={getColor} qru={getQru} id={getId}
                
                setNumber={setNumber} setCity={setCity} setModel={setModel} setManufac={setManufac} 
                setYear={setYear} setColor={setColor} setQru={setQru}>
            </ModalNewPlate>
        </>
    )
}
