import React, { useEffect } from 'react';

function Contact() {

  useEffect(() => {
    // Function to load Google Maps Script
    // const loadScript = (url) => {
    //   const script = document.createElement('script');
    //   script.src = url;
    //   script.async = true;
    //   script.defer = true;
    //   document.body.appendChild(script);
    //   return script;
    // };

    // // Load the script
    // const googleMapScript = loadScript(
    //   'https://maps.googleapis.com/maps/api/js?key=AIzaSyA8eaHt9Dh5H57Zh0xVTqxVdBFCvFMqFjQ&callback=initMap'
    // );

    // // Define the initMap function globally (because callback needs it)
    // window.initMap = function() {
    //   const map = new window.google.maps.Map(document.getElementById('map'), {
    //     zoom: 11,
    //     center: { lat: 40.645037, lng: -73.880224 }
    //   });

    //   const marker = new window.google.maps.Marker({
    //     position: { lat: 40.645037, lng: -73.880224 },
    //     map: map,
    //     icon: process.env.PUBLIC_URL + '/images/maps-and-flags.png' // Correct way to access public images
    //   });
    // };

    // // Clean up (optional but good practice)
    // return () => {
    //   if (googleMapScript) {
    //     googleMapScript.remove();
    //   }
    //   delete window.initMap;
    // };
    
  }, []);

  return (
    <div>
      {/* Contact section */}
      <section className="contact_section layout_padding">
        <div className="d-flex justify-content-center">
          <h2 className="heading_style">Contact us</h2>
        </div>
        <div className="container layout_padding2-top">
          <div className="row">
            <div className="col-md-6">
              <div id="map" className="h-100 w-100" style={{ minHeight: '400px' }}>
              <iframe width="100%" height="100%" className="absolute inset-0" 
              // style="filter: grayscale(1) contrast(1.2) opacity(0.4);" frameborder="0" title="map" marginheight="0" marginwidth="0" 
              // scrolling="no" 
              src="https://maps.google.com/maps?width=100%&amp;height=600&amp;hl=en&amp;q=%C4%B0zmir+(My%20Business%20Name)&amp;ie=UTF8&amp;t=&amp;z=14&amp;iwloc=B&amp;output=embed"></iframe>
              </div>
            </div>
            <div className="col-md-6">
              <div className="contact_form-container">
                <form>
                  <div><input type="text" placeholder="Your Name" /></div>
                  <div><input type="email" placeholder="Your Email" /></div>
                  <div><input type="text" placeholder="Your Phone" /></div>
                  <div><input type="text" className="message_input" placeholder="Message" /></div>
                  <div className="d-flex justify-content-end">
                    <button type="submit" className="">Send</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </section>
      {/* End contact section */}
    </div>
  );
}

export default Contact;
