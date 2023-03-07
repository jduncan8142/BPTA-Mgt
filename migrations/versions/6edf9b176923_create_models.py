"""Create models

Revision ID: 6edf9b176923
Revises: 4df8c5a5c94f
Create Date: 2023-03-06 23:11:56.827730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6edf9b176923'
down_revision = '4df8c5a5c94f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('step',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=False),
    sa.Column('case_id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=96), nullable=False),
    sa.Column('element_id', sa.String(length=1024), nullable=True),
    sa.Column('kwargs', sa.JSON(), nullable=True),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('description', sa.String(length=1024), nullable=False),
    sa.Column('system_metadata', sa.JSON(), nullable=True),
    sa.Column('py_code', sa.String(length=2048), nullable=True),
    sa.ForeignKeyConstraint(['case_id'], ['case.id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=False),
    sa.Column('case_id', sa.Integer(), nullable=True),
    sa.Column('step_id', sa.Integer(), nullable=True),
    sa.Column('test_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('result_type', sa.Enum(), nullable=False),
    sa.Column('result', sa.Enum(), nullable=True),
    sa.ForeignKeyConstraint(['case_id'], ['case.id'], ),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['step_id'], ['step.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('updated', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'updated')
    op.drop_table('result')
    op.drop_table('step')
    # ### end Alembic commands ###