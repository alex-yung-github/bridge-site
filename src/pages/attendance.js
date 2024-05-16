// pages/Attendance.js

import React from 'react';
import { useState } from 'react';

const Attendance = () => {

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(firstName + ' ' + lastName + ' ' + computingID)
  }

  const [firstName, setFirstName] = useState("")
  const [lastName, setLastName] = useState("")
  const [computingID, setComputingID] = useState("")


  return (
    <div className = 'pageBodyBed'>
      <div className = 'pageBodyContainer'>
        <h1 className='pageHeader'>Attendance Form</h1>
        <p>Club attendence for money!</p>

        <form onSubmit={handleSubmit}>
          <label>
            First Name:
            <input type='text' value={firstName} onChange={(e) => setFirstName(e.target.value)} />
          </label>
          <label>
            Last Name:
            <input type='text' value={lastName } onChange={(e) => setLastName(e.target.value)} />
          </label>
          <label>
            Computing ID:
            <input type='text' value={computingID} onChange={(e) => setComputingID(e.target.value)} />
          </label>
          <input type='submit' />
        </form>

      </div>
    </div>
  );
}

export default Attendance;