export default function Header(){
    return (
      <>
<section class="accordion">
  <div class="tab">
    <input type="checkbox" name="accordion-1" id="cb1"/>
    <label for="cb1" class="tab__label">GitLinked</label>
    <div class="tab__content">
      <p>Github based project built in Hackathon</p>
    </div>
  </div>

  <div className="tab">
    <input type="checkbox" name="accordion-1" id="cb2"/>
    <label htmlFor="cb2" className="tab__label">GitLinked</label>
    <div className="tab__content">
      <p>Github based project built in Hackathon</p>
    </div>
  </div>
  <div className="tab">
    <input type="checkbox" name="accordion-1" id="cb3"/>
    <label htmlFor="cb3" className="tab__label">GitLinked</label>
    <div className="tab__content">
      <p>Github based project built in Hackathon</p>
    </div>
  </div>
  <div className="tab">
    <input type="checkbox" name="accordion-1" id="cb4"/>
    <label htmlFor="cb4" className="tab__label">Open multiple</label>
    <div className="tab__content">
    </div>
  </div>
</section>
      </>
    )
}
