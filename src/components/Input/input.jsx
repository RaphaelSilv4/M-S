import PropTypes from 'prop-types'
import Styles from './input.module.css'

export default function Input(props) {

    return (
        <div className={Styles.formControl}>
            <label htmlFor="">{props.label}</label>
            <input 
               type={props.type}
               placeholder={props.placeholder}
               value={props.value}
               onChange={props.onChange}
               required={props.required}
               />
        </div>
    )
}

Input.protTypes = {
    label: PropTypes.string,
    type: PropTypes.string,
    placeholder: PropTypes.string,
    value: PropTypes.string,
    onChange: PropTypes.func,
    required: PropTypes.bool,
}
