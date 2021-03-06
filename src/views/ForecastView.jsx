import React from 'react'
import ISvg from 'react-inlinesvg'

export class ForecastView extends React.Component {
  render() {
    var formattedTime = this.props.clockTimeFormat.format(this.props.time)
    var windDeg = typeof this.props.forecast.wind.deg !== 'undefined' ? this.props.forecast.wind.deg + "°" : ""

    return (
      <div className="ForecastView">
        <div className="weatherHeaderWrapper">
          <div className="weatherTime">
            {formattedTime}
          </div>
          <div className="weatherHeader">
            <div className="weatherImage">
              <img src={this.props.getIcon(this.props.forecast.icon)} />
            </div>
            <div className="weatherTemperature">
              {this.props.forecast.temp}°C
            </div>
          </div>
        </div>
        <div className="weatherDescription">
          {this.props.forecast.description}
        </div>
        <div className="weatherDetails">
          <div className="weatherLocation">
            <ISvg src="/static/weather-icons/place.svg" />{this.props.location}
          </div>
          <div className="weatherWind">
            <ISvg src="/static/weather-icons/wind.svg" />{Math.round(this.props.forecast.wind.speed) + " km/h " + windDeg}
          </div>
        </div>
        <div className="iconsCopyright">
          <p>
            {this.props.getIcon("copyright")}
          </p>
        </div>
      </div>
    )
  }
}

export default ForecastView
