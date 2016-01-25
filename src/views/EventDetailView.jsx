import Paper from 'material-ui/lib/paper'
import React from 'react'

import SpeakerListView from './SpeakerListView'

import QRCode from 'qrcode.react'

export class EventDetailView extends React.Component {

  render () {
    var event = this.props.event
    this.props.addFormattedDatesToEvent(event)

    return (
      <article className={'eventDetails month' + event.month}>
        <div className='headerImageWrapper'>
          <img className='headerImage' src={event.img} />
        </div>
        <h1 className='eventTitle'>
          {event.title}
        </h1>
        <div className='details'>
          <div className='dateInfo'>
            <div className='dateDisplay'>
              <div className='month'>{event.shortMonth}</div>
              <div className='date'>{event.shortDate}</div>
            </div>
          </div>
          <div className='timeLocationInfo'>
            <div className='time'>{event.timeInterval}</div>
            <div className='location'>{event.location}</div>
            {event.speaker ?
              <div className='speaker'>{event.speaker}</div> :
              ''
            }
          </div>
          <div className='QRCodeWrapper'>
            {event.registrationUrl ? <QRCode className='QRCode' value={event.registrationUrl} /> : <div className='QRCode' />}
          </div>
        </div>
        <div className='desc'>{event.desc.split(/\r?\n/).map(function (item, index) {
            return <p key={index}>{item}</p>
          })}
        </div>
        {event.speakers ? <SpeakerListView speakers={event.speakers} /> : ''}
      </article>
    )
  }
}

export default EventDetailView
