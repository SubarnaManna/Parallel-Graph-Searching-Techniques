import React from 'react'
// import { Link } from 'react-router-dom/cjs/react-router-dom.min'
import { Link } from 'react-router-dom/cjs/react-router-dom'
function Header() {
  return (
      // <div className="hero_area">
    <div className='hero_area custom_page-height'>
  {/* <!-- header section strats --> */}
    <section className="header_section">
      <div className="container">
        <nav className="navbar navbar-expand-lg custom_nav-container d-lg-none">
          <a className="navbar-brand" href="#">
            <div className="logo-box">
              <img src="images/logo.png" alt="" />
              <span>
                Logi Map
              </span>
            </div>
          </a>
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>

          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav  ">
              <li className="nav-item active">
                {/* <Link className="nav-link" to="/" >Home <span className="sr-only">(current)</span></Link> */}
                <Link className="nav-link" to="/" >Home</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/about"> About </Link>
              </li>
              <li className="nav-item">
                <a className="nav-link" to="/service"> Service</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" to="/shop"> Shop </a>
              </li>
              <li className="nav-item">
                <a className="nav-link" to="/company"> Company </a>
              </li>
              <li className="nav-item ">
                <a className="nav-link " to="/contact">Contact us</a>
              </li>
            </ul>
          </div>
        </nav>
        <div className="header_container ">
          <div className="logo-box">
            <img src="images/logo.png" alt="" />
            <span>
              Logi Map
            </span>
          </div>
          <div>
            <div className="header_top">
              <div className="header_top-contact">

                <a href="" className="ml-4">
                  <div>
                    <img src="images/phone.png" alt=""  />
                  </div>
                  <span>
                    (+91) 858964785
                  </span>
                </a>
                <a href="" className="ml-4">
                  <div>
                    <img src="images/mail.png" alt=""  />
                  </div>
                  <span>
                    logimap@gmail.com
                  </span>
                </a>
              </div>
              <div className="header_top-social">
                <div>
                  <a href="">
                    <img src="images/fb.png" alt="" />
                  </a>
                </div>
                <div>
                  <a href="">
                    <img src="images/twitter.png" alt="" />
                  </a>
                </div>
                <div>
                  <a href="">
                    <img src="images/g-plus.png" alt="" />
                  </a>
                </div>
                <div>
                  <a href="">
                    <img src="images/linkedin.png" alt="" />
                  </a>
                </div>
              </div>
            </div>
            <div className="header_btm">
              <nav className="navbar navbar-expand-lg custom_nav-container pt-3">

                <button className="navbar-toggler" type="button" data-toggle="collapse"
                  data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                  aria-label="Toggle navigation">
                  <span className="navbar-toggler-icon"></span>
                </button>

                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                  <div className="d-flex mx-auto flex-column flex-lg-row align-items-center">
                    <ul className="navbar-nav  ">
                      <li className="nav-item active">
                        <Link className="nav-link" to="/">Home <span className="sr-only">(current)</span></Link>
                      </li>
                      <li className="nav-item">
                        <Link className="nav-link" to="/about"> About </Link>
                      </li>
                      <li className="nav-item">
                        <Link className="nav-link" to="/service"> Service</Link>
                      </li>
                      <li className="nav-item">
                        <Link className="nav-link" to="/shop"> Shop </Link>
                      </li>
                      <li className="nav-item">
                        <Link className="nav-link" to="/company"> Company </Link>
                      </li>
                      <li className="nav-item ">
                        <Link className="nav-link pr-0" to="/contact">Contact us</Link>
                      </li>
                    </ul>

                  </div>

                </div>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </section>
    {/* <!-- end header section --> */}
    </div>
  )
}

export default Header