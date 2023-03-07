"""Create models

Revision ID: c6950177d489
Revises: 745591115192
Create Date: 2023-03-06 23:16:59.432346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6950177d489'
down_revision = '745591115192'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=False),
    sa.Column('case_id', sa.Integer(), nullable=True),
    sa.Column('step_id', sa.Integer(), nullable=True),
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
    # ### end Alembic commands ###
