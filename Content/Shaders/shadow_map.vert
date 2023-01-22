#version 460 core

layout (location = 2) in vec3 in_position;

uniform mat4 m_Proj;
uniform mat4 m_ViewLight;
uniform mat4 m_Model;

void main() {
    gl_Position = m_Proj * m_ViewLight * m_Model * vec4(in_position, 1.0);
}