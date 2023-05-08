import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faEdit, faCarSide } from '@fortawesome/free-solid-svg-icons'

library.add(faEdit, faCarSide)

export default function PlateCard(props) {

    return(
        <details className='plate-card'>
            <summary> <a>{props.data.number}</a>  <a> {props.data.city}</a> <a>{props.data.manufac} {props.data.model}</a></summary>
            <div className='plate-desc'>
                <a> {props.data.year}</a> 
                <a>{props.data.color}</a>
                <a> {props.data.qru} </a> 
                <FontAwesomeIcon icon="fa-solid fa-edit" className='icon' onClick={props.show}/>
            </div>
        </details> 
    )
}