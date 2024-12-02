import esphome.codegen as cg
from esphome.components import display
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_LAMBDA
from esphome.pins import gpio_output_pin_schema

sevenseg_ns = cg.esphome_ns.namespace("sevenseg")
SEVENSEGComponent = sevenseg_ns.class_("SEVENSEGComponent", cg.PollingComponent)
SEVENSEGComponentRef = SEVENSEGComponent.operator("ref")

CONF_A_PIN = "a_pin"
CONF_B_PIN = "b_pin"
CONF_C_PIN = "c_pin"
CONF_D_PIN = "d_pin"
CONF_E_PIN = "e_pin"
CONF_F_PIN = "f_pin"
CONF_G_PIN = "g_pin"
CONF_DP_PIN = "dp_pin"
CONF_G1_PIN = "g1_pin"
CONF_G2_PIN = "g2_pin"
CONF_G3_PIN = "g3_pin"
CONF_G4_PIN = "g4_pin"
CONF_DIGITS = "digits"

CONFIG_SCHEMA = display.BASIC_DISPLAY_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(SEVENSEGComponent),
        cv.Required(CONF_A_PIN): cv.ensure_schema(gpio_output_pin_schema),
        cv.Required(CONF_B_PIN): cv.ensure_schema(gpio_output_pin_schema),
        cv.Required(CONF_C_PIN): cv.ensure_schema(gpio_output_pin_schema),
        cv.Required(CONF_D_PIN): cv.ensure_schema(gpio_output_pin_schema),
        cv.Required(CONF_E_PIN): cv.ensure_schema(gpio_output_pin_schema),
        cv.Required(CONF_F_PIN): cv.ensure_schema(gpio_output_pin_schema),
        cv.Required(CONF_G_PIN): cv.ensure_schema(gpio_output_pin_schema),
        cv.Required(CONF_DP_PIN): cv.ensure_schema(gpio_output_pin_schema),
        cv.Required(CONF_DIGITS): cv.ensure_list(gpio_output_pin_schema),
    }
).extend(cv.polling_component_schema("25ms"))


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await display.register_display(var, config)

    pin_a = await cg.gpio_pin_expression(config[CONF_A_PIN])
    cg.add(var.set_a_pin(pin_a))
    pin_b = await cg.gpio_pin_expression(config[CONF_B_PIN])
    cg.add(var.set_a_pin(pin_b))
    pin_c = await cg.gpio_pin_expression(config[CONF_C_PIN])
    cg.add(var.set_a_pin(pin_c))
    pin_d = await cg.gpio_pin_expression(config[CONF_D_PIN])
    cg.add(var.set_a_pin(pin_d))
    pin_e = await cg.gpio_pin_expression(config[CONF_E_PIN])
    cg.add(var.set_a_pin(pin_e))
    pin_f = await cg.gpio_pin_expression(config[CONF_F_PIN])
    cg.add(var.set_a_pin(pin_f))
    pin_g = await cg.gpio_pin_expression(config[CONF_G_PIN])
    cg.add(var.set_a_pin(pin_g))
    pin_dp = await cg.gpio_pin_expression(config[CONF_DP_PIN])
    cg.add(var.set_a_pin(pin_dp))

    digits = []
    for pin in config[CONF_DIGITS]:
        pin_digit = await cg.gpio_pin_expression(pin)
        digits.append(pin_digit)
    cg.add(var.set_digits(digits))

    if CONF_LAMBDA in config:
        lambda_ = await cg.process_lambda(
            config[CONF_LAMBDA], [(SEVENSEGComponentRef, "it")], return_type=cg.void
        )
        cg.add(var.set_writer(lambda_))
