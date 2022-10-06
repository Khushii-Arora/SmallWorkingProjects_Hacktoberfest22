import React, { useState, useContext } from 'react'
import {GlobalContext} from '../Context/GlobalState'
import {v4} from 'uuid'

const AddTransaction = () => {
    const [text, setText] = useState("")
    const [amount, setAmount] = useState(0)
    const {addTransaction} = useContext(GlobalContext);
    const Submit = e => {
        e.preventDefault();
        const newTransaction ={
            id: v4(),
            text,
            amount: +amount
        }
        addTransaction(newTransaction);
        setAmount(0);
        setText("")
    }
    return (
        <div>
            <h3>Add new Transaction</h3>
            <form onSubmit={Submit}>
                <div className="form-control">
                    <label htmlFor="text">Text</label>
                    <input type="text" value={text} onChange={(e)=> (setText(e.target.value))} id="text" placeholder="Enter a text.." />
                </div>
                <div className="form-control">
                    <label htmlFor="amount">
                        Amount <br/>
                    </label>
                    <input type="number" value={amount} onChange={(e)=> (setAmount(e.target.value))} placeholder="Enter Amount..." />
                </div>
                <button className="btn">Add Transaction</button>
            </form>
        </div>
    )
}

export default AddTransaction
