import React from 'react';
import Index from '.';
import About from './about';
import Service from './service';
import Company from './company';
import Contact from './contact';
import Shop from './shop';

function Combine() {
  return (
    <div>
        <Index/>
        <About/>
        <Service/>
        <Shop/>
        <Company/>
        <Contact/>
    </div>
  )
}

export default Combine